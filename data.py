from enum import Enum
from dataclasses import dataclass

SORT_BY_URL_PARAMETER_NAME = "sort_by"
PAGE_NUMBER_URL_PARAMETER_NAME = "page"
PAGE_SIZE_URL_PARAMETER_NAME = "page_size"
DEFAULT_SORT_BY = "name"
DEFAULT_PAGE_NUMBER = 0
DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 20
WEAPONS_REPOSITORY_JSON_PATH = "data/weapons.json"
ARMORS_REPOSITORY_JSON_PATH = "data/armors.json"
NPC_REPOSITORY_FILE_PATH = "data/npc.json"


class WeaponType(str, Enum):
    SWORD = "sword"
    AXE = "axe"
    BOW = "bow"
    CROSSBOW = "crossbow"


class Guild(str, Enum):
    MERCENARY = "mercenary"
    DRAGON_HUNTER = "dragon hunter"
    MILITIA = "militia"
    PALADIN = "paladin"
    NOVICE = "novice"
    MAGICIAN = "magician"
    NEUTRAL = "neutral"


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
    id: str


@dataclass
class NPC:
    name: str
    hp: int
    mana: int
    guild: str
    equipment: list[str]
    id: str
