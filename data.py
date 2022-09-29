from enum import Enum
from dataclasses import dataclass

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
    type: str
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