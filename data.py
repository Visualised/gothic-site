from enum import Enum

class WeaponType(Enum):
    SWORD = "sword"
    AXE = "axe"
    BOW = "bow"
    CROSSBOW = "crossbow"

weapons_list = [
    {
    "id": "P4nKuuuurtk4-z-nwidii-k000x",
    "name": "Zardzewiały miecz", 
    "damage": 10, 
    "required_strength": 5,
    "required_dexterity": 0,
    },
    {
    "id": "Jaa444-ni3-chc3-tyl3-z4r4bi4c",
    "name": "Miecz Świstaka", 
    "damage": 20, 
    "required_strength": 15,
    "required_dexterity": 0,
    },
    {
    "id": "pies3k-szcz3sl1wy",
    "name": "Miecz strachu", 
    "damage": 42, 
    "required_strength": 18,
    "required_dexterity": 0,
    },
    {
    "id": "eeeeeeeeeeeeeeeeeeee",
    "name": "Miecz śmierci", 
    "damage": 48, 
    "required_strength": 21,
    "required_dexterity": 0,
    },
    {
    "id": "j3st-d0w0d-n4-t0-ajdi",
    "name": "Miecz Blizny", 
    "damage": 85, 
    "required_strength": 70,
    "required_dexterity": 0,
    },
]