from cache.src.port.inport.CacheUseCase import CacheService
from cache.src.exceptions.NotFoundException import NotFoundException
from cache.src.persistence.domain.Pokemon import Pokemon
from cache.src.algorithm.DoublyLinkedListImpl import DoublyLinkedList
from collections import defaultdict
import json
import abc

class EvictionPolicy(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getKey(self):
        pass
    
    @abc.abstractmethod
    def addKey(self, key):
        pass
    
class LRUEvictionPolicy(EvictionPolicy):
    
    def __init__(self):
        self.least_recently_used = DoublyLinkedList()
    
    def getKey(self):
        #returns the key at the beginning
        key = self.least_recently_used.head.data
        if key is None:
            throw NotFoundException()
        return key
    
    def addKey(self,key):
        self.least_recently_used.addAtLast(key)
        
        
class LFUEvictionPolicy(EvictionPolicy):
    
    def getKey():
        pass

class CacheServiceImpl(CacheService):
    def __init__(self, capacity, EvictionPolicy lruPolicy):
        self.capacity = capacity
        
        self.cache = defaultdict(Pokemon)
        #self.least_recently_used = DoublyLinkedList()
        self.evictionPolicy = lruPolicy
        # implementing the LRU mechanism using the cache.

    def get(self, key):
        if key not in self.cache.keys():
            raise NotFoundException("not found")
        self.least_recently_used.removeAtBeginning()
        self.least_recently_used.insertAtEnd(key)
        print(self.cache[key])
        return self.cache[key].asdict()

    def delete(self, key):
        if key not in self.cache.keys():
            raise NotFoundException()
        self.cache.pop(key)

    def put(self, key, value):
        
        if len(self.cache) >= self.capacity:
            self.evict()

        if key in self.cache.keys():
            self.least_recently_used.removeAtBeginning()
            
        self.cache[key] = Pokemon(**value)  # value
        self.least_recently_used.insertAtEnd(key)

    def evict(self):
        # identify a way to evict the cache using lru and then add the new elements
        lru_element = self.least_recently_used.removeAtBeginning()
        self.delete(lru_element)

    def __str__(self):
        return self.cache.__str__()

    def list_all(self):
        li = []
        for k, v in self.cache.items():
            li.append(v.asdict())
        return li

    def clear(self):
        self.least_recently_used = DoublyLinkedList()
        self.cache = {}
