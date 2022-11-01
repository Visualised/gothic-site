from data import Armor
from repositories.base import AbstractJSONRepository, AbstractDBRepository
from models.armors import ArmorDBModel


class JSONArmorsRepository(AbstractJSONRepository):
    def __init__(self, json_file_path: str) -> None:
        super().__init__(json_file_path)

    MODEL = Armor
    SORTED_BY = {
        "price": lambda x: x.price,
        "magic_resistance": lambda x: x.magic_resistance,
        "fire_resistance": lambda x: x.fire_resistance,
        "ranged_resistance": lambda x: x.ranged_resistance,
        "weapon_resistance": lambda x: x.weapon_resistance,
        "name": lambda x: x.name.lower(),
    }


class DBArmorsRepository(AbstractDBRepository):
    DB_MODEL = ArmorDBModel
    ORDER_BY = {
        "id": ArmorDBModel.id,
        "name": ArmorDBModel.name,
        "weapon_resistance": ArmorDBModel.weapon_resistance,
        "ranged_resistance": ArmorDBModel.ranged_resistance,
        "fire_resistance": ArmorDBModel.fire_resistance,
        "magic_resistance": ArmorDBModel.magic_resistance,
        "price": ArmorDBModel.price,
    }
