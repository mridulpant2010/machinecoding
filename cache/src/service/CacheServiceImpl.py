from cache.src.port.inport.CacheUseCase import CacheService
from cache.src.exceptions.NotFoundException import NotFoundException


class CacheServiceImpl(CacheService):
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = dict()
        self.least_recently_used = []
        # implementing the LRU mechanism using the cache.

    def get(self, key):
        if key not in self.cache.keys():
            raise NotFoundException("not found")

        self.least_recently_used.remove(key)
        self.least_recently_used.append(key)
        return self.cache[key]

    def delete(self, key):
        if key not in self.cache.keys():
            raise NotFoundException()
        return self.cache.pop(key)

    def put(self, key, value):
        # but what about the eviction policy also
        if len(self.cache) >= self.capacity:
            self.evict(key)
        
        if key in self.cache.keys():
            self.least_recently_used.remove(key)
            
        self.cache[key] = value
        self.least_recently_used.append(key)

    def evict(self, key):
        # identify a way to evict the cache using lru and then add the new elements
        lru_element = self.least_recently_used.pop(0)
        self.delete(lru_element)

    def __str__(self):
        return self.cache.__str__()
    
    def clear(self):
        self.least_recently_used=[] 
        self.cache={}
