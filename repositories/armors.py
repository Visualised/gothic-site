import uuid, json
from api_errors import ObjectDoesNotExist
from data import Armor
from dataclasses import asdict

json_file_path = "data/armors.json"

class JSONArmorsRepository:
    def __init__(self, json_file_path: str) -> None:
        self._armors_dataclass_list = []
        self._json_in_memory = self.read_from_json(json_file_path)
        self._json_file_path = json_file_path
        
        for armor in self._json_in_memory:
            self._armors_dataclass_list.append(Armor(**armor))

    @staticmethod
    def read_from_json(json_file_path: str):
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_to_json(self, json_file_path: str):
        with open(json_file_path, "w+", encoding="utf-8") as f:
            armors_list = [asdict(armor) for armor in self._armors_dataclass_list]
            json.dump(armors_list, f, indent=2)

    def list(self):
        return self._json_in_memory

    def get(self, id: str):
        founded_armor = [armor for armor in self._armors_dataclass_list if armor.id == id]
        if not founded_armor:
            raise ObjectDoesNotExist
            
        return founded_armor[0]

    def add(self, json_user_data: dict):
        json_user_data["id"] = str(uuid.uuid4())

        self._armors_dataclass_list.append(Armor(**json_user_data))
        self.save_to_json(self._json_file_path)

    def update(self, id, json_user_data: dict):
        old_armor = self.get(id)
        old_armor_index = self._armors_dataclass_list.index(old_armor)
        self._armors_dataclass_list[old_armor_index] = Armor(**json_user_data, id=old_armor.id)
        
        self.save_to_json(self._json_file_path)

    def delete(self, id: str):
        self.get(id)

        self._armors_dataclass_list = [i for i in self._armors_dataclass_list if i.id != id]
        self.save_to_json(self._json_file_path)


# not updated for type hinting and handlers, for inheritance demonstration only
class InMemoryArmorsRepository:

    def __init__(self, armors_list) -> None:
        self._armors_list = armors_list
        
    def list(self):
        return self._armors_list

    def get(self, id):
        armor = list(filter(lambda x: x["id"] == id, self._armors_list))
        return armor[0] if armor else None

    def add(self, json_user_data):
        json_user_data["id"] = str(uuid.uuid4())
        self._armors_list.append(json_user_data)
        return True

    def update(self, id, json_data):
        armor = self.get(id)
        if not armor or not self.verify_type(json_data):
            return False

        armor.update(json_data) 
        return True

    def delete(self, id):
        armor = self.get(id)
        if not armor:
            return False

        self._armors_list = [i for i in self._armors_list if i["id"] != id]
        return True

armors_repository = JSONArmorsRepository(json_file_path)