import unittest
from unittest.mock import Mock, patch
from repositories.weapons import JSONWeaponsRepository
from repositories.armors import JSONArmorsRepository
from repositories.npc import JSONNPCRepository
from controllers.npc_controller import NPCController


class Test_NPCController(unittest.TestCase):
    def setUp(self):
        pass
