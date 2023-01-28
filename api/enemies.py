from flask import request
from flask.views import MethodView
from http import HTTPStatus
from data import (
    SORT_BY_URL_PARAMETER_NAME,
    PAGE_NUMBER_URL_PARAMETER_NAME,
    PAGE_SIZE_URL_PARAMETER_NAME,
    DEFAULT_SORT_BY,
    DEFAULT_PAGE_NUMBER,
    DEFAULT_PAGE_SIZE,
)


class EnemiesAPI(MethodView):
    def __init__(self, enemies_controller):
        self.enemies_controller = enemies_controller

    def get(self, id: str):
        if id:
            location = self.enemies_controller.get(id)
            return location, HTTPStatus.OK
        else:
            sort_by = request.args.get(SORT_BY_URL_PARAMETER_NAME, DEFAULT_SORT_BY)
            page = request.args.get(PAGE_NUMBER_URL_PARAMETER_NAME, DEFAULT_PAGE_NUMBER)
            page_size = request.args.get(PAGE_SIZE_URL_PARAMETER_NAME, DEFAULT_PAGE_SIZE)
            try:
                return self.enemies_controller.list(sort_by, int(page), int(page_size)), HTTPStatus.OK
            except ValueError:
                return "page and page_size parameters needs to be int", HTTPStatus.BAD_REQUEST

    def post(self):
        json_data = request.get_json()
        self.enemies_controller.add(json_data)
        return "Enemy has been added", HTTPStatus.CREATED

    def patch(self, id: str):
        json_data = request.get_json()
        self.enemies_controller.update(id, json_data)
        return "Enemy has been updated", HTTPStatus.OK

    def delete(self, id: str):
        self.enemies_controller.delete(id)
        return "Enemy has been deleted", HTTPStatus.OK
