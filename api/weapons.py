from flask import request
from flask.views import MethodView
from http import HTTPStatus
from repositories.weapons import JSONWeaponsRepository, DBWeaponsRepository
from dataclasses import asdict
from data import (
    SORT_BY_URL_PARAMETER_NAME,
    PAGE_NUMBER_URL_PARAMETER_NAME,
    PAGE_SIZE_URL_PARAMETER_NAME,
    DEFAULT_SORT_BY,
    DEFAULT_PAGE_NUMBER,
    DEFAULT_PAGE_SIZE,
)


class WeaponsAPI(MethodView):
    def __init__(self, weapons_controller):
        self.weapons_controller = weapons_controller

    def get(self, id: str):
        if id:
            weapon = self.weapons_controller.get(id)
            return weapon, HTTPStatus.OK
        else:
            sort_by = request.args.get(SORT_BY_URL_PARAMETER_NAME, DEFAULT_SORT_BY)
            page = request.args.get(PAGE_NUMBER_URL_PARAMETER_NAME, DEFAULT_PAGE_NUMBER)
            page_size = request.args.get(PAGE_SIZE_URL_PARAMETER_NAME, DEFAULT_PAGE_SIZE)
            try:
                return self.weapons_controller.list(sort_by, int(page), int(page_size)), HTTPStatus.OK
            except ValueError:
                return "page and page_size parameters needs to be int", HTTPStatus.BAD_REQUEST

    def post(self):
        json_data = request.get_json()
        self.weapons_controller.add(json_data)
        return "Weapon has been added", HTTPStatus.CREATED

    def patch(self, id: str):
        json_data = request.get_json()
        self.weapons_controller.update(id, json_data)
        return "Weapon has been updated", HTTPStatus.OK

    def delete(self, id: str):
        self.weapons_controller.delete(id)
        return "Weapon has been deleted", HTTPStatus.OK
