import pytest
import sys,json
sys.path.append("C:/Users/mridul/OneDrive/Documents/GitHub/machinecoding/")
from cache.src.port.inport.CacheUseCase import CacheService
from cache.src.exceptions.NotFoundException import NotFoundException
from cache.src.persistence.domain.Pokemon import Pokemon
from cache.src.service.CacheServiceImpl import CacheServiceImpl  # Import your CacheServiceImpl class

@pytest.fixture
def cache():
    return CacheServiceImpl(capacity=2)

def test_put_and_get(cache):
    pokemon1 = {"id":"1","name":"pikachu","type":"raichu","height":"3","weight":"20","abilities":"can sink"}
    cache.put('1', pokemon1)
    result1 = cache.get('1')
    assert result1 == pokemon1

    # Adding another item, which should trigger eviction
    pokemon2 = {"id":"2","name":"Bulbasaur","type":"raichu","height":"3","weight":"20","abilities":"can sink"} 
    cache.put('2', pokemon2)

    pokemon3 = {"id":"3","name":"Bulbasaur","type":"raichu","height":"3","weight":"20","abilities":"can sink"} 
    cache.put('3', pokemon3)
    #The 'Pikachu' item should have been evicted
    with pytest.raises(NotFoundException):
        cache.get('1')

    result2 = cache.get('2')
    assert result2 == pokemon2

def test_delete(cache):
    pokemon1 = {'id': '1', 'name': 'Pikachu'}
    cache.put('1', pokemon1)
    cache.delete('1')
    with pytest.raises(NotFoundException):
        cache.get('1')

def test_evict(cache):
    cache.put('1', {'id': '1', 'name': 'Pikachu'})
    cache.put('2', {'id': '2', 'name': 'Bulbasaur'})
    cache.put('3', {'id': '3', 'name': 'Charmander'})
    
    # After the 'Pikachu' item was added, it should have been evicted
    with pytest.raises(NotFoundException):
        cache.get('1')

    # The 'Bulbasaur' and 'Charmander' items should be in the cache
    assert cache.get('2')['name'] == 'Bulbasaur'
    assert cache.get('3')['name'] == 'Charmander'

def test_clear(cache):
    cache.put('1', {'id': '1', 'name': 'Pikachu'})
    cache.clear()
    assert len(cache.least_recently_used) == 0
    assert len(cache.cache) == 0
