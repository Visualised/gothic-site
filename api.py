from flask import Flask, request
from http import HTTPStatus
from repositories import swords_repository

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/swords")
def print_sword_list():
    return swords_repository.list(), HTTPStatus.OK

@app.route("/swords/<id>")
def print_sword_details(id):
    sword = swords_repository.get(id)
    if not sword:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND
    return sword, HTTPStatus.OK

@app.route("/swords", methods=["POST"])
def add_sword():
    json_data = request.get_json()
    swords_repository.add(json_data)
    return "Sword has been added", HTTPStatus.CREATED

@app.route("/swords/<id>", methods=["PATCH"])
def update_sword(id):
    json_data = request.get_json()
    is_updated = swords_repository.update(id, json_data)
    if is_updated:
        return "Sword has been updated", HTTPStatus.OK
    else:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND

@app.route("/swords/<id>", methods=["DELETE"])
def delete_sword(id):
    is_deleted = swords_repository.delete(id)
    if is_deleted:
        return "Sword has been deleted", HTTPStatus.OK
    else:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND

if __name__ == "__main__":
    app.run()