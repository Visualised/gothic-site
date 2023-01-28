from data import NPC, Guild
from api_errors import WrongGuild
from repositories.base import AbstractJSONRepository, AbstractDBRepository
from models.npc import NPCDBModel


class JSONNPCRepository(AbstractJSONRepository):
    def __init__(self, json_file_path: str) -> None:
        super().__init__(json_file_path)

    MODEL = NPC
    SORTED_BY = {
        "name": lambda x: x.name.lower(),
        "hp": lambda x: x.hp,
        "guild": lambda x: x.guild.lower(),
        "mana": lambda x: x.mana,
    }

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["guild"] = Guild(json_user_data["guild"].lower())
        except (ValueError, KeyError):
            raise WrongGuild


class DBNPCRepository(AbstractDBRepository):
    DB_MODEL = NPCDBModel
    ORDER_BY = {
        "id": NPCDBModel.id,
        "name": NPCDBModel.name,
        "hp": NPCDBModel.hp,
        "mana": NPCDBModel.mana,
        "guild": NPCDBModel.guild,
        "weapon_id": NPCDBModel.weapon_id,
        "armor_id": NPCDBModel.armor_id,
    }

    @staticmethod
    def clean_data(json_user_data: dict):
        try:
            json_user_data["guild"] = Guild(json_user_data["guild"].lower())
        except ValueError:
            raise WrongGuild
        except KeyError:
            pass
