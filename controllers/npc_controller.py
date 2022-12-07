from dataclasses import asdict
from services.random_avatar_service import RandomAvatarService


class NPCController:
    def __init__(self, npc_repository, weapons_repository, armors_repository) -> None:
        self.npc_repository = npc_repository
        self.weapons_repository = weapons_repository
        self.armors_repository = armors_repository
        self.random_avatar_service = RandomAvatarService()

    def replace_equipment_data(self, npc_to_edit):
        npc_to_edit_copy = asdict(npc_to_edit)

        READ_EQUIPMENT_DATA = {
            "weapon": self.weapons_repository.get,
            "armor": self.armors_repository.get,
        }

        try:
            for current_index, item in enumerate(npc_to_edit_copy["equipment"]):
                item_type, item_id = item.split(":")
                if item_type in READ_EQUIPMENT_DATA.keys():
                    equipment_data = READ_EQUIPMENT_DATA[item_type](item_id)
                    npc_to_edit_copy["equipment"][current_index] = equipment_data

            return npc_to_edit_copy
        except KeyError:
            return npc_to_edit_copy

    def get(self, id: str):
        clear_data = self.replace_equipment_data(self.npc_repository.get(id))

        return clear_data

    def list(self, sort_by: str, page: int, page_size: int, limit_result: bool = False):
        sorted_list = self.npc_repository.list(sort_by, page, page_size)

        for current_index, npc in enumerate(sorted_list):
            sorted_list[current_index] = self.replace_equipment_data(npc)

        # robie to w ten sposób ponieważ robiąc to na poziomie sqlalchemy select query w base.py
        # stracimy zwrotke jako model bazy danych a przez to pare wartości key:value
        # otrzymując same wartości poszczególnych kolumn. Mam wątpliwości do co skalowalności
        # WRÓCIĆ - dałoby się to zrobić przez list/dict comprehension
        if limit_result:
            limited_sorted_list = []
            for row in sorted_list:
                filtered_row = {"id": row["id"], "name": row["name"]}
                limited_sorted_list.append(filtered_row)

            return limited_sorted_list

        return sorted_list

    def add(self, json_user_data: dict):
        avatar_link = self.random_avatar_service.get()
        json_user_data["avatar"] = avatar_link
        self.npc_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        self.npc_repository.update(id, json_user_data)

    def delete(self, id: str):
        self.npc_repository.delete(id)
