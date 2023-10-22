import pytest
import sys,json
sys.path.append("C:/Users/mridul/OneDrive/Documents/GitHub/machinecoding/")
from cache.src.controller.CacheController import app
from cache.src.service.CacheServiceImpl import CacheServiceImpl
from cache.src.persistence.domain.Pokemon import Pokemon

@pytest.fixture
def client():
    app.config["TESTING"] = True
    client = app.test_client()
    cache_use_case = CacheServiceImpl(4)
    yield client, cache_use_case

# def test_get_cache_items_by_key(client):
#     # how can i have a builder pattern in python
#     client, cache_use_case = client
#     #given
#     pokemon = Pokemon.PokemonBuilder().with_id("1").with_name("pikachu").with_height("5").with_weight("10").with_abilities("swim").with_type("raichu").build()    
#     print(pokemon.asdict())
#     #then 
#     cache_use_case.put("1",pokemon.asdict())
    
#     response = client.get("/app/v1/cache/items/1")
#     print(response)
#     data = json.loads(response.data.decode("utf-8"))
#     print(data)
#     assert response.status_code == 200
    
def test_get_cache_items_by_key_when_key_exists(client, monkeypatch):
    # Mock the cache_use_case for testing
    class MockCache:
        def get(self, key):
            return {key: "your_data"}

    monkeypatch.setattr(app, 'cache_use_case', MockCache())

    # When: Making a GET request with an existing key
    response = client.get("/app/v1/cache/items/data")

    # Then: Verify the response
    assert response.status_code == 200
    assert response.get_json() == {"data": "your_data"}
    
    
def test_get_cache_items_non_exsiting_key(client):
    client, cache_use_case = client
    response = client.get("/app/v1/cache/items/2")
    assert response.status_code == 404
    
    
    
