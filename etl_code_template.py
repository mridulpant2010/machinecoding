class Conf:
    def __init__(self):
        self.setup_glue_conf()
        self.setup_spark_conf()
        self.setup_s3_conf()

    def setup_glue_conf(self):
        self._glue_context = GlueContext(SparkContext.getOrCreate())
        args = getResolvedOptions(sys.argv, ['JOB_NAME', 
                                        'target_bucket',
                                        'target_database',
                                        'tenant_env'
                                        ])
        for key in args:
            key_new = '_' + key
            setattr(self, key_new, args[key])

        self._job = Job(self._glue_context)
        self._job.init(args['JOB_NAME'], args)

    def setup_spark_conf(self):
        self._spark = self._glue_context.sparkSession
        self._spark.conf.set('spark.sql.sources.partitionOverwriteMode', 'dynamic')
        #self._spark.conf.set('spark.sql.files.maxRecordsPerFile', 500000)
        self._spark.conf.set('spark.sql.crossJoin.enabled', 'true')
        self._spark.conf.set("spark.sql.legacy.parquet.int96RebaseModeInRead", "LEGACY")
        self._spark.conf.set("spark.sql.legacy.parquet.int96RebaseModeInWrite", "LEGACY")
        self._spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInRead", "LEGACY")
        self._spark.conf.set("spark.sql.legacy.parquet.datetimeRebaseModeInWrite", "LEGACY")

    def setup_s3_conf(self):
        self.s3 = boto3.resource('s3')
        self.s3_client = boto3.client('s3')
        s3_path_prefix = f's3://{self._target_bucket}/main/castrol/{self._target_database}/{output_table}/'
        s3_key = 'dh_audit_source_system_id=SAPPRL/'
        self.s3_path_with_key=s3_path_prefix+s3_key






class Extraction():
    def __init__(self,tenant_env,conf):
        self._tenant_env = tenant_env
        self._transform_env_mapping = {
            'dev': 'ws00an',
            'test': 'ws00am',
            'preprod': 'ws00all',
            'prod': 'ws00ak'
        }
        self.conf = conf

    def initialize_mapping(self):
        if self._tenant_env in self._transform_env_mapping:
            print(self._tenant_env)
            self._transform_latest_prl = f'{self._transform_env_mapping[self._tenant_env]}_transform_latest_prl'
        else:
            sys.exit('Invalid environment')

    def extract_glue_table(self,database,table_name):
        glue_table = self.conf._glue_context.create_dynamic_frame.from_catalog(
            database=database,
            table_name=table_name,
        ).toDF()

    def extract_glue_table(self,database,table_name,predicate_columns,col_names):
        glue_table = self.conf._glue_context.create_dynamic_frame.from_catalog(
            database=database,
            table_name=table_name,
            push_down_predicate=predicate_columns,
        ).toDF().select(
            *[col(cols) for cols in col_names]
        )




class Transformation:
    def __init__(self,conf,extract):
        self.conf = conf
        self.extract = extract 
        self._table_conf = [
            {'table_name':'','database':'','push_down_predicate':'','columns':''}

        ]

    def generate_all_tables_df(self):
        for each_table in self._table_conf:
            f'{each_table['database']_each_table['table_name']}' = self.extract.extract_glue_table(**each_table)

    def prepare_staging_df(self):
        input_databases = [self._transform_latest_prl,]
        input_tables = ['bsik', 'bsak']

        output_database = 'conform_main_castrol'
        output_table = 'accounts_payable_item'

        delta_raw_df = self.load_data_from_catalog(input_databases, input_tables)
        staging_df = (
            delta_raw_df
                .join(broadcast(self.currency.alias('currency')),
                      [
                          'currency_code',
                          #'dh_audit_source_system_id'
                      ], how='left_outer')
                .join(broadcast(self.document_currency.alias('document_currency')),
                      [
                          'document_currency_code',
                          #'dh_audit_source_system_id'
                      ], how='left_outer')
                .join(broadcast(self.company.alias('company')),
                      [
                          'company_code',
                          'dh_audit_source_system_id'
                      ], how='left_outer')
                .join(broadcast(self.vendor.alias('vendor')),
                      [
                          'vendor_code',
                          'dh_audit_source_system_id'
                      ], how='left_outer')
                .join(broadcast(self.local_document_type_tvakt.alias('ldt_tvakt')),
                      [
                          'local_document_type_code',
                          'dh_audit_source_system_id'
                      ], how='left_outer')
                .join(broadcast(self.local_document_type_t003t.alias('ldt_t003t')),
                      [
                          'local_document_type_code',
                          'dh_audit_source_system_id'
                      ], how='left_outer')                      
                .select(
                md5(concat(*primary_key)).alias('accounts_payable_document_item_id'),
                col('accounts_payable_document_code').cast(StringType()),
                col('accounts_payable_document_item_code').cast(StringType()),
                col('mnemonic_code').cast(StringType()),
                col('fiscal_year').cast(IntegerType()),
                col('clearing_date').cast(TimestampType()),
                col('posting_date').cast(TimestampType()),
                col('due_date').cast(TimestampType()),
                col('net_value').cast(DecimalType(38,8)),
                col('net_value_in_document_currency').cast(DecimalType(38,8)),
                col('net_value_in_second_local_currency').cast(DecimalType(38,8)),
                lit('0').alias('accounting_document_item_id').cast(StringType()),
                coalesce(col('vendor.vendor_id'), lit('0')).alias('vendor_id').cast(StringType()),
                coalesce(col('company.company_id'), lit('0')).alias('company_id').cast(StringType()),
                coalesce(col('currency.currency_id'), lit('0')).alias('currency_id').cast(StringType()),
                coalesce(col('document_currency.currency_id'), lit('0')).alias('document_currency_id').cast(StringType()),
                coalesce(coalesce(col('ldt_tvakt.local_document_type_id'), col('ldt_t003t.local_document_type_id')), lit('0')).alias('accounting_document_type_id').cast(StringType()),
                lit('INSERT').alias('dh_audit_record_type'),
                lit(record_timestamp).alias('dh_audit_record_timestamp').cast(TimestampType()),
                col('dh_audit_source_system_id').cast(StringType()),
                lit(None).alias('dh_audit_user_updated').cast(StringType()),
                lit(None).alias('dh_audit_batch_id').cast(StringType()),
                col('dh_audit_start_timestamp').cast(TimestampType()),
                lit('9999-12-31 00:00:00').alias('dh_audit_end_timestamp').cast(TimestampType()),
                lit('1').alias('dh_audit_active_record')
            )
        )


    def load_data_from_catalog(self, databases, tables):
        output_dfs = []
        for database in databases:
            for table_name in tables:
                raw_df = self.extract._glue_context.create_dynamic_frame.from_catalog(
                    database=database,
                    table_name=table_name
                ).select_fields(
                    [
                        'di_operation_type',
                        'belnr',
                        'buzei',
                        'gjahr',
                        'augdt',
                        'budat',
                        'zfbdt',
                        'zbd1t',
                        'dmbtr',
                        'wrbtr',
                        'dmbe2',
                        'lifnr',
                        'bukrs',
                        'waers',
                        'pswsl',
                        'blart',
                        'shkzg',
                        'creation_date',
                        'mandt',
                        'umsks',
                        'umskz',
                        'augbl',
                        'zuonr',
                    ]
                ).toDF()

                raw_df = raw_df.filter(col('di_operation_type').isin(['I','U']))
                cast_df = (
                    raw_df
                        .select(
                        col('belnr'),
                        col('buzei'),
                        col('gjahr'),
                        col('augdt'),
                        col('budat'),
                        col('zfbdt'),
                        col('zbd1t').cast(IntegerType()),
                        col('dmbtr'),
                        col('wrbtr'),
                        col('dmbe2'),
                        col('lifnr'),
                        col('bukrs'),
                        col('waers'),
                        col('pswsl'),
                        col('blart'),
                        col('shkzg'),
                        col('creation_date'),
                        coalesce(col('mandt').cast(StringType()),lit('0')).alias('mandt'),
                        coalesce(col('umsks').cast(StringType()),lit('0')).alias('umsks'),
                        coalesce(col('umskz').cast(StringType()),lit('0')).alias('umskz'),
                        coalesce(col('augbl').cast(StringType()),lit('0')).alias('augbl'),
                        coalesce(col('zuonr').cast(StringType()),lit('0')).alias('zuonr'),
                    )
                )

                delta_df = (
                    cast_df
                        .select(
                        col('belnr').alias('accounts_payable_document_code'),
                        concat_ws('-',*[col('buzei'),col('augbl'),col('zuonr'),col('umsks'),col('umskz'),col('mandt')]).alias('accounts_payable_document_item_code'),
                        col('belnr').alias('mnemonic_code'),
                        col('gjahr').alias('fiscal_year'),
                        col('augdt').alias('clearing_date'),
                        col('budat').alias('posting_date'),
                        expr('date_add(zfbdt,zbd1t)').alias('due_date'),
                        when(col('shkzg') == 'H', col('dmbtr') * -1).otherwise(col('dmbtr')).alias('net_value'),
                        col('wrbtr').alias('net_value_in_document_currency'),
                        col('dmbe2').alias('net_value_in_second_local_currency'),
                        col('lifnr').alias('vendor_code'),
                        col('bukrs').alias('company_code'),
                        col('waers').alias('currency_code'),
                        col('pswsl').alias('document_currency_code'),
                        col('blart').alias('local_document_type_code'),
                        col('creation_date').alias('dh_audit_start_timestamp'),
                        lit('SAPPRL').alias('dh_audit_source_system_id'),
                        )
                    )

                output_dfs.append(delta_df)

        return reduce(DataFrame.unionByName, output_dfs)


class Load:
    def __init__(self,conf,transform):
        self.transform = transform 
        self.conf = conf

    def write_to_s3(self):
        sink = self.conf._glue_context.getSink(connection_type='s3',
            path=self.conf.s3_path_prefix,
            enableUpdateCatalog=True,
            updateBehavior="UPDATE_IN_DATABASE",
            partitionKeys = ['dh_audit_source_system_id'])

        sink.setFormat('glueparquet')
        sink.setCatalogInfo(catalogDatabase=output_database, catalogTableName=output_table)

        print(f'pruge {s3_path_with_key}')
        self.conf._glue_context.purge_s3_path(
            s3_path_with_key,
            {'retentionPeriod': 0, 'excludeStorageClasses': ()}
        )
        staging_df_dynf = DynamicFrame.fromDF(self.transform.staging_df, self.conf._glue_context,output_table)
        sink.writeFrame(staging_df_dynf)


class Main:
    def __init__(self):
        self.conf = Conf()

    def execute(self):
        self.extract = Extraction(self.conf)
        self.transform = Transformation(self.conf,extract)
        Load(conf,self.transform)
