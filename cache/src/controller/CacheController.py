from flask import Flask,jsonify,request
from cache.src.exceptions.NotFoundException import NotFoundException
from cache.src.port.inport.CacheUseCase import CacheUseCase

app  = Flask(__name__)

cache_use_case = CacheUseCase()

@app.route('/app/v1/cache/items/<int:key>',methods=['GET'])
def get_cache_items_by_key(key):
    try:
        result = cache_use_case.get(key)
    except NotFoundException:
        return None,404
    
    return jsonify(result),200

@app.route('/app/v1/cache/add-items/',methods=['POST'])
def update_cache_items():
    try:
        data = request.get_json()
        key = data['key']
        value = data['value']
        result_add = cache_use_case.put(key, value)
    except NotFoundException:
        return None,404
    except Exception as e:
        pass
    return jsonify(result_add),201
    
@app.route('/app/v1/cache/remove/<int:key>',methods=['DELETE'])
def delete_cache(key):
    try:
        op =  cache_use_case.remove_cache(key)
    except NotFoundException:
        return None,404
    return jsonify(op),200