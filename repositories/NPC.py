from data import DEFAULT_PAGE_NUMBER, DEFAULT_PAGE_SIZE, NPC, Guild
from api_errors import WrongGuild
from repositories.base import AbstractJSONRepository
from data import (
    MAX_PAGE_SIZE,
    DEFAULT_PAGE_SIZE,
    DEFAULT_PAGE_NUMBER,
)


class JSONNPCRepository(AbstractJSONRepository):
    def __init__(self, json_file_path: str) -> None:
        super().__init__(json_file_path)

    MODEL = NPC
    SORTED_BY = {
        "name": lambda x: x["name"],
        "hp": lambda x: x["hp"],
        "guild": lambda x: x["guild"],
        "mana": lambda x: x["mana"],
    }

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["guild"] = Guild(json_user_data["guild"])
        except ValueError:
            raise WrongGuild

    def list(self, npc_list: list, sort_by: str, page: int, page_size: int):

        if sort_by[0] == "-":
            is_reversed = True
            sort_by = sort_by[1:]
        else:
            is_reversed = False

        if page < 0:
            page = DEFAULT_PAGE_NUMBER

        if page_size <= 0:
            page_size = DEFAULT_PAGE_SIZE

        if page_size > MAX_PAGE_SIZE:
            page_size = MAX_PAGE_SIZE

        start = page * page_size
        end = (page + 1) * page_size

        sorted_list = sorted(npc_list, key=self.SORTED_BY[sort_by], reverse=is_reversed)
        return sorted_list[start:end]
