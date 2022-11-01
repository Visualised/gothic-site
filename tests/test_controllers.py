import unittest
from unittest.mock import Mock, patch
from repositories.weapons import JSONWeaponsRepository
from repositories.armors import JSONArmorsRepository
from repositories.npc import JSONNPCRepository
from controllers.npc_controller import NPCController

JSON_FILE_PATH_WEAPONS = "tests/fixtures/test_weapons_data.json"
JSON_FILE_PATH_ARMORS = "tests/fixtures/test_armors_data.json"
JSON_FILE_PATH_NPC = "tests/fixtures/test_npc_data.json"


class Test_NPCController(unittest.TestCase):
    def setUp(self):
        self.npc_repository = JSONNPCRepository(JSON_FILE_PATH_NPC)
        self.weapons_repository = JSONWeaponsRepository(JSON_FILE_PATH_ARMORS)
        self.armors_repository = JSONArmorsRepository(JSON_FILE_PATH_ARMORS)
        self.npc_controller = NPCController(self.npc_repository, self.weapons_repository, self.armors_repository)
        self.npc_id = "ddac20ed-8033-44b1-b67e-51cd9341fee9"
        pass

    def get_dataclass_list_from_repository(self):
        return self.npc_controller.npc_repository._dataclass_list.copy()

    def test_get(self):
        reponse_from_controller = self.npc_controller.get(self.npc_id)
