import sys

sys.path.append("C:/Users/mridul/OneDrive/Documents/GitHub/machinecoding/")
from cache.src.service.CacheServiceImpl import CacheServiceImpl

if __name__ == "__main__":
    cache = CacheServiceImpl(5)
    cache.put(1, "value1")
    cache.put(2, "value2")
    cache.put(3, "value3")
    cache.put(4, "value4")
    cache.put(5, "value5")
    print(cache)
    print(cache.get(1))
    print(cache.get(2))
    print(cache.get(3))
    print(cache)
    cache.put(6, "value6")
    cache.put(7, "value7")
    print(cache)
