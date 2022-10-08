from flask import request, Blueprint
from http import HTTPStatus
from repositories.armors import armors_repository
from dataclasses import asdict
from data import (
    SORT_BY_URL_PARAMETER_NAME,
    PAGE_NUMBER_URL_PARAMETER_NAME,
    PAGE_SIZE_URL_PARAMETER_NAME,
    DEFAULT_SORT_BY,
    DEFAULT_PAGE_NUMBER,
    DEFAULT_PAGE_SIZE,
)

armors_router = Blueprint("armors_router", __name__, url_prefix="/armors")


@armors_router.route("")
def print_armor_list():
    sort_by = request.args.get(SORT_BY_URL_PARAMETER_NAME, DEFAULT_SORT_BY)
    page = request.args.get(PAGE_NUMBER_URL_PARAMETER_NAME, DEFAULT_PAGE_NUMBER)
    page_size = request.args.get(PAGE_SIZE_URL_PARAMETER_NAME, DEFAULT_PAGE_SIZE)
    try:
        return armors_repository.list(sort_by, int(page), int(page_size)), HTTPStatus.OK
    except ValueError:
        return "page and page_size parameters needs to be int", HTTPStatus.BAD_REQUEST


@armors_router.route("/<id>")
def print_armor_details(id: str):
    armor = asdict(armors_repository.get(id))
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
