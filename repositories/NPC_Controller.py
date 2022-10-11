import json
from dataclasses import asdict
from data import (
    WEAPONS_REPOSITORY_JSON_PATH,
    ARMORS_REPOSITORY_JSON_PATH,
)


class NPC_Controller:
    def __init__(self, npc_repository) -> None:
        self.npc_repository = npc_repository

    @staticmethod
    def read_from_json(json_file_path: str):
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                temp_data = json.load(f)
                return temp_data
        except FileNotFoundError:
            return []

    @staticmethod
    def get_object_from_json_data(json_data, id: str):
        return [object for object in json_data if object["id"] == id]

    READ_EQUIPMENT_DATA = {
        "armor": read_from_json(ARMORS_REPOSITORY_JSON_PATH),
        "weapon": read_from_json(WEAPONS_REPOSITORY_JSON_PATH),
    }

    def replace_equipment_data(self, npc):  # chciałbym zobaczyć bardziej elegancki sposób na te metode
        npc_to_edit = asdict(npc)  # if is_dataclass(npc) else npc ? dziala bez tego więc usunąłem
        equipment_list = npc_to_edit["equipment"]
        for current_index, item in enumerate(equipment_list):
            if type(item) == str:
                item_type, item_id = item.split(":")
                if item_type in self.READ_EQUIPMENT_DATA.keys():
                    equipment_data = self.READ_EQUIPMENT_DATA[item_type]
                    object_to_replace_with = self.get_object_from_json_data(equipment_data, item_id)
                    npc_to_edit["equipment"][current_index] = object_to_replace_with[0]
        return npc_to_edit

    def get(self, id: str):
        return self.replace_equipment_data(self.npc_repository.get(id))

    def list(self, sort_by: str, page: int, page_size: int):
        data_with_replaced_equipment = []
        for npc in self.npc_repository._dataclass_list:
            data_with_replaced_equipment.append(self.replace_equipment_data(npc))
        return self.npc_repository.list(data_with_replaced_equipment, sort_by, page, page_size)

    def add(self, json_user_data: dict):
        self.npc_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        self.npc_repository.update(id, json_user_data)

    def delete(self, id: str):
        self.npc_repository.delete(id)
