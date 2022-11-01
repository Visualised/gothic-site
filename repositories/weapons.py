from data import WeaponType, Weapon
from api_errors import WrongType
from repositories.base import AbstractJSONRepository, AbstractDBRepository
from models.weapons import WeaponDBModel
from models.base import db


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


class DBWeaponsRepository(AbstractDBRepository):
    DB_MODEL = WeaponDBModel
    ORDER_BY = {
        "damage": WeaponDBModel.damage,
        "required_strength": WeaponDBModel.required_strength,
        "required_dexterity": WeaponDBModel.required_dexterity,
        "name": WeaponDBModel.name,
        "id": WeaponDBModel.id,
    }

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["type"] = WeaponType(json_user_data["type"].lower())
        except (ValueError, KeyError):
            raise WrongType
