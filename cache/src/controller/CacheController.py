from flask import Flask, jsonify, request, abort
import sys

sys.path.append("C:/Users/mridul/OneDrive/Documents/GitHub/machinecoding/")
from cache.src.exceptions.NotFoundException import NotFoundException
from cache.src.service.CacheServiceImpl import CacheServiceImpl

app = Flask(__name__)

capacity = 4
cache_use_case = CacheServiceImpl(4)

"""
TODO
- loggers are missing, add them to proper place
- authentication is missing 
- how will we make it concurrent , 
    - use of threadpool executor
- understand when to throw and which error.
- use of async and await 

"""

# threading is for working in parallel, async is for waiting in parallel.
# https://www.youtube.com/watch?v=Ii7x4mpIhIs


@app.route("/app/v1/cache/items/<string:key>", methods=["GET"])
def get_cache_items_by_key(key):
    print(f"key is {key}")
    try:
        result = cache_use_case.get(key)
    except NotFoundException:
        abort(404)

    return jsonify(result), 200


@app.route("/app/v1/cache/add-items/", methods=["POST"])
def update_cache_items():
    try:
        data = request.get_json()
        print(data)
        key = data["key"]
        value = data["value"]
        print(key, value)
        result_add = cache_use_case.put(key, value)
    except NotFoundException:
        abort(404)
    return jsonify(result_add), 201


@app.route("/app/v1/cache/remove/<string:key>", methods=["DELETE"])
def delete_cache(key):
    try:
        op = cache_use_case.delete(key)
    except NotFoundException:
        abort(404)
    return jsonify(op), 200


@app.route("/app/v1/cache/list/all", methods=["GET"])
def list_all():
    op = cache_use_case.list_all()
    return jsonify(op), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
