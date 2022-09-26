from flask import request, Blueprint
from http import HTTPStatus
from repositories.armors import armors_repository

armors_router = Blueprint("armors_router", __name__, url_prefix="/armors")

@armors_router.route("")
def print_armor_list():
    return armors_repository.list(), HTTPStatus.OK

@armors_router.route("/<id>")
def print_armor_details(id: str):
    armor = armors_repository.get(id)
    return armor, HTTPStatus.OK

@armors_router.route("", methods=["POST"])
def add_armor():
    json_data = request.get_json()
    armors_repository.add(json_data)
    return "Armor has been added", HTTPStatus.CREATED

@armors_router.route("/<id>", methods=["PATCH"])
def update_armor(id: str):
    json_data = request.get_json()
    armors_repository.update(id, json_data)
    return "Armor has been updated", HTTPStatus.OK

@armors_router.route("/<id>", methods=["DELETE"])
def delete_armor(id: str):
    armors_repository.delete(id)
    return "Armor has been deleted", HTTPStatus.OK