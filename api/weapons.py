from flask import request, Blueprint
from http import HTTPStatus
from repositories.weapons import weapons_repository
from dataclasses import asdict
import data

weapons_router = Blueprint("weapons_router", __name__, url_prefix="/weapons")


@weapons_router.route("")
def print_weapon_list():
    sort_by = request.args.get(data.SORT_BY_URL_PARAMETER_NAME, data.DEFAULT_SORT_BY)
    page = request.args.get(data.PAGE_NUMBER_URL_PARAMETER_NAME, data.DEFAULT_PAGE_NUMBER)
    page_size = request.args.get(data.PAGE_SIZE_URL_PARAMETER_NAME, data.DEFAULT_PAGE_SIZE)
    try:
        return weapons_repository.list_sorted_by(sort_by, int(page), int(page_size)), HTTPStatus.OK
    except:
        return "Wrong URL parameters", HTTPStatus.BAD_REQUEST
        

@weapons_router.route("/<id>")
def print_weapon_details(id: str):
    weapon = asdict(weapons_repository.get(id))
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
