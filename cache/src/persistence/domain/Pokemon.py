class Pokemon:
    def __init__(self, id, name, type, height, weight, abilities):
        self._id = id
        self._name = name
        self._type = type
        self._height = height
        self._weight = weight
        self._abilities = abilities

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        self._type = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def abilities(self):
        return self._abilities

    @abilities.setter
    def abilities(self, value):
        self._abilities = value

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        self._weight = value

    def asdict(self):
        return {
            "_id": self._id,
            "_abilities": self._abilities,
            "_name": self._name,
            "_type": self._type,
            "_height": self._height,
            "_weight": self._weight,
        }
