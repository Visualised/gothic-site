from data import WeaponType, Weapon
from api_errors import ObjectDoesNotExist, WrongType
from dataclasses import asdict
import uuid, json

json_file_path = "data/weapons.json"


class JSONWeaponsRepository:
    def __init__(self, json_file_path: str) -> None:
        self._weapons_dataclass_list = self.read_from_json(json_file_path)
        self._json_file_path = json_file_path

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["type"] = WeaponType(json_user_data["type"])
        except ValueError:
            raise WrongType

    def read_from_json(self, json_file_path: str):
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                temp_data = json.load(f)
                temp_list = []
                for weapon in temp_data:
                    self.clean_data(weapon)
                    temp_list.append(Weapon(**weapon))
                return temp_list
        except FileNotFoundError:
            return []

    def save_to_json(self, json_file_path: str):
        with open(json_file_path, "w+", encoding="utf-8") as f:
            weapons_list = [asdict(weapon) for weapon in self._weapons_dataclass_list]
            json.dump(weapons_list, f, indent=2)

    def list(self):
        return self._weapons_dataclass_list

    def get(self, id: str):
        founded_weapon = [weapon for weapon in self._weapons_dataclass_list if weapon.id == id]
        if not founded_weapon:
            raise ObjectDoesNotExist

        return founded_weapon[0]

    def add(self, json_user_data: dict):
        json_user_data["id"] = str(uuid.uuid4())
        self.clean_data(json_user_data)

        self._weapons_dataclass_list.append(Weapon(**json_user_data))
        self.save_to_json(self._json_file_path)

    def update(self, id, json_user_data: dict):
        self.clean_data(json_user_data)
        old_weapon = self.get(id)
        old_weapon_index = self._weapons_dataclass_list.index(old_weapon)
        self._weapons_dataclass_list[old_weapon_index] = Weapon(**json_user_data, id=old_weapon.id)

        self.save_to_json(self._json_file_path)

    def delete(self, id: str):
        self.get(id)

        self._weapons_dataclass_list = [i for i in self._weapons_dataclass_list if i.id != id]
        self.save_to_json(self._json_file_path)

    def list_sorted_by(self, sort_by: str):
        SORTED_BY = {
            "damage": lambda x: x.damage,
            "required_strength": lambda x: x.required_strength,
            "required_dexterity": lambda x: x.required_dexterity,
            "name": lambda x: x.name,
        }

        if sort_by[0] == "-":
            is_reversed = True
            sort_by = sort_by[1:]
        else:
            is_reversed = False

        return sorted(self._weapons_dataclass_list, key=SORTED_BY[sort_by], reverse=is_reversed)


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
