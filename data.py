from enum import Enum
# from dataclasses import dataclass

class WeaponType(str, Enum):
    SWORD = "sword"
    AXE = "axe"
    BOW = "bow"
    CROSSBOW = "crossbow"

# tu bym chciał zacząć robić dataklasy
# @dataclass
# class Weapon:
#     name: str
#     damage: int
#     required_strength: int
#     required_dexterity: int
#     type: str
#     id: str