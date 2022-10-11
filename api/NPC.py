from flask import request
from flask.views import MethodView
from http import HTTPStatus
from repositories.NPC import JSONNPCRepository
from repositories.NPC_Controller import NPC_Controller
from data import (
    SORT_BY_URL_PARAMETER_NAME,
    PAGE_NUMBER_URL_PARAMETER_NAME,
    PAGE_SIZE_URL_PARAMETER_NAME,
    DEFAULT_SORT_BY,
    DEFAULT_PAGE_NUMBER,
    DEFAULT_PAGE_SIZE,
)


class NPCAPI(MethodView):
    def __init__(self, npc_repository: JSONNPCRepository):
        super().__init__()
        self.npc_controller = NPC_Controller(npc_repository)

    def get(self, id: str):
        if id:
            npc = self.npc_controller.get(id)
            return npc, HTTPStatus.OK
        else:
            sort_by = request.args.get(SORT_BY_URL_PARAMETER_NAME, DEFAULT_SORT_BY)
            page = request.args.get(PAGE_NUMBER_URL_PARAMETER_NAME, DEFAULT_PAGE_NUMBER)
            page_size = request.args.get(PAGE_SIZE_URL_PARAMETER_NAME, DEFAULT_PAGE_SIZE)
            try:
                return self.npc_controller.list(sort_by, int(page), int(page_size)), HTTPStatus.OK
            except ValueError:
                return "page and page_size parameters needs to be an int", HTTPStatus.BAD_REQUEST

    def post(self):
        json_data = request.get_json()
        self.npc_controller.add(json_data)
        return "NPC has been added", HTTPStatus.CREATED

    def patch(self, id: str):
        json_data = request.get_json()
        self.npc_controller.update(id, json_data)
        return "NPC has been updated", HTTPStatus.OK

    def delete(self, id: str):
        self.npc_controller.delete(id)
        return "NPC has been deleted", HTTPStatus.OK
