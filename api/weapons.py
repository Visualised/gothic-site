from flask import request, Blueprint
from http import HTTPStatus
from repositories.weapons import weapons_repository

weapons_router = Blueprint("weapons_router", __name__, url_prefix="/weapons")

@weapons_router.route("")
def print_weapon_list():
    return weapons_repository.list(), HTTPStatus.OK

@weapons_router.route("/<id>")
def print_weapon_details(id: str):
    weapon = weapons_repository.get(id)
    return weapon, HTTPStatus.OK

@weapons_router.route("", methods=["POST"])
def add_weapon():
    json_data = request.get_json()
    weapons_repository.add(json_data)
    return "Weapon has been added", HTTPStatus.CREATED

@weapons_router.route("/<id>", methods=["PATCH"])
def update_weapon(id: str):
    json_data = request.get_json()
    weapons_repository.update(id, json_data)
    return "Weapon has been updated", HTTPStatus.OK


@weapons_router.route("/<id>", methods=["DELETE"])
def delete_weapon(id: str):
    weapons_repository.delete(id)
    return "Weapon has been deleted", HTTPStatus.OK