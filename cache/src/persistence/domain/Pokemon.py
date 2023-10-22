class Pokemon:        
    def __init__(self, id=None, name=None, type=None, height=None, weight=None, abilities=None):
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
            "id": self._id,
            "abilities": self._abilities,
            "name": self._name,
            "type": self._type,
            "height": self._height,
            "weight": self._weight,
        }

    class PokemonBuilder:
        
        def __init__(self):
            self.pokemon = Pokemon()
        
        def with_abilities(self,abilities):
            self.pokemon.abilities = abilities
            return self
        def with_name(self,name):
            self.pokemon.name = name
            return self
        def with_type(self,type):
            self.pokemon.type = type
            return self
        def with_height(self,height):
            self.pokemon.height = height
            return self
        def with_weight(self,weight):
            self.pokemon.weight = weight
            return self
        def with_id(self,id):
            self.pokemon.id = id
            return self
        def build(self):
            return self.pokemon
            