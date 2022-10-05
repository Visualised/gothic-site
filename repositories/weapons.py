from data import WeaponType, Weapon
from api_errors import WrongType
from repositories.base import AbstractJSONRepository
import uuid

json_file_path = "data/weapons.json"


class JSONWeaponsRepository(AbstractJSONRepository):
    def __init__(self, json_file_path: str) -> None:
        super().__init__(json_file_path)

    MODEL = Weapon
    SORTED_BY = {
        "damage": lambda x: x.damage,
        "required_strength": lambda x: x.required_strength,
        "required_dexterity": lambda x: x.required_dexterity,
        "name": lambda x: x.name,
    }

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["type"] = WeaponType(json_user_data["type"])
        except ValueError:
            raise WrongType

    def update(self, id, json_user_data: dict):
        self.clean_data(json_user_data)
        old_weapon = self.get(id)
        old_weapon_index = self._dataclass_list.index(old_weapon)

        self._dataclass_list[old_weapon_index] = self.MODEL(**json_user_data, id=old_weapon.id)
        self.save_to_json(self._json_file_path)

    def add(self, json_user_data: dict):
        json_user_data["id"] = str(uuid.uuid4())
        self.clean_data(json_user_data)

        self._dataclass_list.append(self.MODEL(**json_user_data))
        self.save_to_json(self._json_file_path)


weapons_repository = JSONWeaponsRepository(json_file_path)
