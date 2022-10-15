from dataclasses import asdict
from data import NPC


class NPCController:
    def __init__(self, npc_repository, weapons_repository, armors_repository) -> None:
        self.npc_repository = npc_repository
        self.weapons_repository = weapons_repository
        self.armors_repository = armors_repository

    def replace_equipment_data(self, npc_to_edit):
        npc_to_edit_copy = NPC(**asdict(npc_to_edit))

        READ_EQUIPMENT_DATA = {
            "weapon": self.weapons_repository.get,
            "armor": self.armors_repository.get,
        }

        for current_index, item in enumerate(npc_to_edit_copy.equipment):
            item_type, item_id = item.split(":")
            if item_type in READ_EQUIPMENT_DATA.keys():
                equipment_data = READ_EQUIPMENT_DATA[item_type](item_id)
                npc_to_edit_copy.equipment[current_index] = equipment_data

        return npc_to_edit_copy

    def get(self, id: str):
        return self.replace_equipment_data(self.npc_repository.get(id))

    def list(self, sort_by: str, page: int, page_size: int):
        sorted_list = self.npc_repository.list(sort_by, page, page_size)

        for current_index, npc in enumerate(sorted_list):
            sorted_list[current_index] = self.replace_equipment_data(npc)

        return sorted_list

    def add(self, json_user_data: dict):
        self.npc_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        self.npc_repository.update(id, json_user_data)

    def delete(self, id: str):
        self.npc_repository.delete(id)
