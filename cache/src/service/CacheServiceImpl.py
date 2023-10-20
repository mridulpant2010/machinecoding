from cache.src.port.inport.CacheUseCase import CacheService
from cache.src.exceptions.NotFoundException import NotFoundException
from cache.src.persistence.domain.Pokemon import Pokemon
from collections import defaultdict
import json

class CacheServiceImpl(CacheService):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = defaultdict(Pokemon)
        self.least_recently_used = []
        # implementing the LRU mechanism using the cache.

    def get(self, key):
        if key not in self.cache.keys():
            raise NotFoundException("not found")
        print(f"inside the get CacheServiceImpl method: {key}")
        self.least_recently_used.remove(key)
        self.least_recently_used.append(key)
        print(self.cache[key])
        return self.cache[key].__dict__

    def delete(self, key):
        if key not in self.cache.keys():
            raise NotFoundException()
        self.cache.pop(key)

    def put(self, key, value):
        
        if len(self.cache) >= self.capacity:
            self.evict()

        if key in self.cache.keys():
            self.least_recently_used.remove(key)

        self.cache[key] = Pokemon(**value)  # value
        self.least_recently_used.append(key)

    def evict(self):
        # identify a way to evict the cache using lru and then add the new elements
        lru_element = self.least_recently_used.pop(0)
        self.delete(lru_element)

    def __str__(self):
        return self.cache.__str__()

    def list_all(self):
        li = []
        for k, v in self.cache.items():
            li.append(v.asdict())
        return li

    def clear(self):
        self.least_recently_used = []
        self.cache = {}
