from flask import Flask, request
from http import HTTPStatus
from repositories import weapons_repository

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/weapons")
def print_weapon_list():
    return weapons_repository.list(), HTTPStatus.OK

@app.route("/weapons/<id>")
def print_weapon_details(id):
    weapon = weapons_repository.get(id)
    if not weapon:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND
    else:
        return weapon, HTTPStatus.OK

@app.route("/weapons", methods=["POST"])
def add_weapon():
    json_data = request.get_json()
    is_added = weapons_repository.add(json_data)
    if is_added:
        return "Weapon has been added", HTTPStatus.CREATED
    else:
        return "Wepon hasn't been added, wrong type", HTTPStatus.BAD_REQUEST

@app.route("/weapons/<id>", methods=["PATCH"])
def update_weapon(id):
    json_data = request.get_json()
    is_updated = weapons_repository.update(id, json_data)
    if is_updated:
        return "Weapon has been updated", HTTPStatus.OK
    else:
        return "Weapon hasn't been updated", HTTPStatus.BAD_REQUEST

@app.route("/weapons/<id>", methods=["DELETE"])
def delete_weapon(id):
    is_deleted = weapons_repository.delete(id)
    if is_deleted:
        return "Weapon has been deleted", HTTPStatus.OK
    else:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND

if __name__ == "__main__":
    app.run()