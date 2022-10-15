from data import WeaponType, Weapon
from api_errors import WrongType
from repositories.base import AbstractJSONRepository


class JSONWeaponsRepository(AbstractJSONRepository):
    def __init__(self, json_file_path: str) -> None:
        super().__init__(json_file_path)

    MODEL = Weapon
    SORTED_BY = {
        "damage": lambda x: x.damage,
        "required_strength": lambda x: x.required_strength,
        "required_dexterity": lambda x: x.required_dexterity,
        "name": lambda x: x.name.lower(),
    }

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["type"] = WeaponType(json_user_data["type"].lower())
        except (ValueError, KeyError):
            raise WrongType
