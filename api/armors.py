from flask import request, Blueprint
from http import HTTPStatus
from repositories.armors import armors_repository

armors_router = Blueprint("armors_router", __name__, url_prefix="/armors")

@armors_router.route("")
def print_armor_list():
    return armors_repository.list(), HTTPStatus.OK

@armors_router.route("/<id>")
def print_armor_details(id):
    armor = armors_repository.get(id)
    if not armor:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND
    else:
        return armor, HTTPStatus.OK

@armors_router.route("", methods=["POST"])
def add_armor():
    json_data = request.get_json()
    is_added = armors_repository.add(json_data)
    if is_added:
        return "Armor has been added", HTTPStatus.CREATED
    else:
        return "Armor hasn't been added, wrong type", HTTPStatus.BAD_REQUEST

@armors_router.route("/<id>", methods=["PATCH"])
def update_armor(id):
    json_data = request.get_json()
    is_updated = armors_repository.update(id, json_data)
    if is_updated:
        return "Armor has been updated", HTTPStatus.OK
    else:
        return "Armor hasn't been updated", HTTPStatus.BAD_REQUEST

@armors_router.route("/<id>", methods=["DELETE"])
def delete_armor(id):
    is_deleted = armors_repository.delete(id)
    if is_deleted:
        return "Armor has been deleted", HTTPStatus.OK
    else:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND