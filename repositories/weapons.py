from data import WeaponType
from api_errors import ObjectDoesNotExist, WrongType
import uuid, json

json_file_path = "data/weapons.json"

class JSONWeaponsRepository:
    def __init__(self, json_file_path: str) -> None:
        self._json_in_memory = self.read_from_json(json_file_path)
        self._json_file_path = json_file_path

    def read_from_json(self, json_file_path: str):
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_to_json(self, json_file_path: str):
        with open(json_file_path, "w+", encoding="utf-8") as f:
            json.dump(self._json_in_memory, f, indent=2)

    def is_valid_type(self, json_user_data: dict):
        try:
            json_user_data["type"] = WeaponType(json_user_data["type"])
        except ValueError:
            raise WrongType

    def list(self):
        return self._json_in_memory

    def get(self, id: str):
        weapon = list(filter(lambda x: x["id"] == id, self._json_in_memory))
        if not weapon:
            raise ObjectDoesNotExist
            
        return weapon[0]

    def add(self, json_user_data: dict):
        json_user_data["id"] = str(uuid.uuid4())
        self.is_valid_type(json_user_data)

        self._json_in_memory.append(json_user_data)
        self.save_to_json(self._json_file_path)

    def update(self, id, json_user_data: dict):
        self.is_valid_type(json_user_data)
        weapon = self.get(id)
        
        weapon.update(json_user_data)
        self.save_to_json(self._json_file_path)

    def delete(self, id: str):
        self.get(id)

        self._json_in_memory = [i for i in self._json_in_memory if i["id"] != id]
        self.save_to_json(self._json_file_path)


# not updated for type hinting and handlers, for inheritance demonstration only
class InMemoryWeaponsRepository:

    def __init__(self, weapons_list) -> None:
        self._weapons_list = weapons_list
        
    def list(self):
        return self._weapons_list

    def get(self, id):
        weapon = list(filter(lambda x: x["id"] == id, self._weapons_list))
        return weapon[0] if weapon else None

    def add(self, json_user_data):
        json_user_data["id"] = str(uuid.uuid4())
        try:
            json_user_data["type"] = WeaponType(json_user_data["type"])
        except ValueError:
            return False
        self._weapons_list.append(json_user_data)
        return True

    def update(self, id, json_data):
        weapon = self.get(id)
        if not weapon or not self.verify_type(json_data):
            return False

        weapon.update(json_data) 
        return True

    def delete(self, id):
        weapon = self.get(id)
        if not weapon:
            return False

        self._weapons_list = [i for i in self._weapons_list if i["id"] != id]
        return True

weapons_repository = JSONWeaponsRepository(json_file_path)