from enum import Enum
from dataclasses import dataclass

SORT_BY_URL_PARAMETER_NAME = "sort"
DEFAULT_SORT_BY = "name"
PAGE_NUMBER_URL_PARAMETER_NAME = "page"
DEFAULT_PAGE_NUMBER = 0
PAGE_SIZE_URL_PARAMETER_NAME = "page_size"
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 2


class WeaponType(str, Enum):
    SWORD = "sword"
    AXE = "axe"
    BOW = "bow"
    CROSSBOW = "crossbow"


@dataclass
class Weapon:
    name: str
    damage: int
    required_strength: int
    required_dexterity: int
    type: WeaponType
    id: str


@dataclass
class Armor:
    name: str
    weapon_resistance: int
    ranged_resistance: int
    fire_resistance: int
    magic_resistance: int
    price: int
    id: int
