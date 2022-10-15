import unittest
from unittest.mock import patch, Mock
from api_errors import ObjectDoesNotExist, WrongGuild, WrongType
from repositories.weapons import JSONWeaponsRepository
from repositories.armors import JSONArmorsRepository
from repositories.npc import JSONNPCRepository

JSON_FILE_PATH_WEAPONS = "tests/fixtures/test_weapons_data.json"
JSON_FILE_PATH_ARMORS = "tests/fixtures/test_armors_data.json"
JSON_FILE_PATH_NPC = "tests/fixtures/test_npc_data.json"


class Test_JSONWeaponsRepository(unittest.TestCase):
    def setUp(self):
        self.weapons_repository = JSONWeaponsRepository(JSON_FILE_PATH_WEAPONS)
        self.first_id = self.weapons_repository._dataclass_list[0].id
        self.mock_json_user_data = {
            "name": "Testowy Miecz",
            "damage": 60,
            "required_strength": 22,
            "required_dexterity": 0,
            "type": "sword",
        }

    def test_get(self):
        self.assertTrue(self.weapons_repository.get(self.first_id))

        with self.assertRaises(ObjectDoesNotExist):
            self.weapons_repository.get("bad id")

    def test_clean_data(self):
        self.mock_json_user_data["type"] = "bad type"

        with self.assertRaises(WrongType):
            self.weapons_repository.clean_data(self.mock_json_user_data)

    @patch("repositories.weapons.JSONWeaponsRepository.save_to_json")
    def test_add(self, mock_save_to_json: Mock):
        list_before_addition = self.weapons_repository._dataclass_list
        self.weapons_repository.add(self.mock_json_user_data)

        self.assertEqual(list_before_addition, self.weapons_repository._dataclass_list)
        mock_save_to_json.assert_called_once()

    @patch("repositories.weapons.JSONWeaponsRepository.save_to_json")
    def test_delete(self, mock_save_to_json: Mock):
        old_list = self.weapons_repository._dataclass_list
        self.weapons_repository.delete(self.first_id)

        self.assertNotEqual(old_list, self.weapons_repository._dataclass_list)
        mock_save_to_json.assert_called_once()

    @patch("repositories.weapons.JSONWeaponsRepository.save_to_json")
    def test_update(self, mock_save_to_json: Mock):
        old_weapon = self.weapons_repository.get(self.first_id)
        self.weapons_repository.update(self.first_id, self.mock_json_user_data)
        updated_weapon = self.weapons_repository.get(self.first_id)

        self.assertNotEqual(old_weapon, updated_weapon)
        mock_save_to_json.assert_called_once()

    def test_list_sorted_by(self):
        mock_sort_by = "name"
        mock_page_number = 0
        mock_page_size = 10
        sorted_list = self.weapons_repository.list(mock_sort_by, mock_page_number, mock_page_size)

        self.assertEqual(sorted_list[0].name, "aaaaTestowy Miecz Trzy")

    def test_list_sorted_by_descending(self):
        mock_sort_by = "-name"
        mock_page_number = 0
        mock_page_size = 10
        sorted_list = self.weapons_repository.list(mock_sort_by, mock_page_number, mock_page_size)

        self.assertEqual(sorted_list[0].name, "ffffWielki Mjeczyk")


class Test_JSONArmorsRepository(unittest.TestCase):
    def setUp(self):
        self.armors_repository = JSONArmorsRepository(JSON_FILE_PATH_ARMORS)
        self.first_id = self.armors_repository._dataclass_list[0].id
        self.mock_json_user_data = {
            "name": "Testowy Armor",
            "weapon_resistance": 40,
            "ranged_resistance": 30,
            "fire_resistance": 20,
            "magic_resistance": 10,
            "price": 666,
        }

    def test_get(self):
        self.assertTrue(self.armors_repository.get(self.first_id))

        with self.assertRaises(ObjectDoesNotExist):
            self.armors_repository.get("bad id")

    @patch("repositories.armors.JSONArmorsRepository.save_to_json")
    def test_add(self, mock_save_to_json: Mock):
        list_before_addition = self.armors_repository._dataclass_list
        self.armors_repository.add(self.mock_json_user_data)

        self.assertEqual(list_before_addition, self.armors_repository._dataclass_list)
        mock_save_to_json.assert_called_once()

    @patch("repositories.armors.JSONArmorsRepository.save_to_json")
    def test_delete(self, mock_save_to_json: Mock):
        old_list = self.armors_repository._dataclass_list
        self.armors_repository.delete(self.first_id)

        self.assertNotEqual(old_list, self.armors_repository._dataclass_list)
        mock_save_to_json.assert_called_once()

    @patch("repositories.armors.JSONArmorsRepository.save_to_json")
    def test_update(self, mock_save_to_json: Mock):
        old_armor = self.armors_repository.get(self.first_id)
        self.armors_repository.update(self.first_id, self.mock_json_user_data)
        updated_armor = self.armors_repository.get(self.first_id)

        self.assertNotEqual(old_armor, updated_armor)
        mock_save_to_json.assert_called_once()

    def test_list_sorted_by(self):
        mock_sort_by = "name"
        mock_page_number = 0
        mock_page_size = 10
        sorted_list = self.armors_repository.list(mock_sort_by, mock_page_number, mock_page_size)

        self.assertEqual(sorted_list[0].name, "aaaaaaaSuper Armor")

    def test_list_sorted_by_descending(self):
        mock_sort_by = "-name"
        mock_page_number = 0
        mock_page_size = 10
        sorted_list = self.armors_repository.list(mock_sort_by, mock_page_number, mock_page_size)

        self.assertEqual(sorted_list[0].name, "eeeeeeeWilczy Armor")


class Test_JSONNPCRepository(unittest.TestCase):
    def setUp(self):
        self.npc_repository = JSONNPCRepository(JSON_FILE_PATH_NPC)
        self.first_id = self.npc_repository._dataclass_list[0].id
        self.mock_json_user_data = {
            "name": "Canthar",
            "hp": 260,
            "mana": 25,
            "guild": "neutral",
            "equipment": ["weapon:65017267-oczy-4079-8b74-760cbc575b45", "armor:345cc691-b59f-4860-8ba0-418b9ae8a672"],
        }

    def test_get(self):
        self.assertTrue(self.npc_repository.get(self.first_id))

        with self.assertRaises(ObjectDoesNotExist):
            self.npc_repository.get("bad id")

    def test_clean_data(self):
        self.mock_json_user_data["guild"] = "bad type"

        with self.assertRaises(WrongGuild):
            self.npc_repository.clean_data(self.mock_json_user_data)

    @patch("repositories.npc.JSONNPCRepository.save_to_json")
    def test_add(self, mock_save_to_json: Mock):
        list_before_addition = self.npc_repository._dataclass_list
        self.npc_repository.add(self.mock_json_user_data)

        self.assertEqual(list_before_addition, self.npc_repository._dataclass_list)
        mock_save_to_json.assert_called_once()

    @patch("repositories.npc.JSONNPCRepository.save_to_json")
    def test_delete(self, mock_save_to_json: Mock):
        old_list = self.npc_repository._dataclass_list
        self.npc_repository.delete(self.first_id)

        self.assertNotEqual(old_list, self.npc_repository._dataclass_list)
        mock_save_to_json.assert_called_once()

    @patch("repositories.npc.JSONNPCRepository.save_to_json")
    def test_update(self, mock_save_to_json: Mock):
        old_weapon = self.npc_repository.get(self.first_id)
        self.npc_repository.update(self.first_id, self.mock_json_user_data)
        updated_weapon = self.npc_repository.get(self.first_id)

        self.assertNotEqual(old_weapon, updated_weapon)
        mock_save_to_json.assert_called_once()

    def test_list_sorted_by(self):
        mock_sort_by = "name"
        mock_page_number = 0
        mock_page_size = 10
        sorted_list = self.npc_repository.list(mock_sort_by, mock_page_number, mock_page_size)

        self.assertEqual(sorted_list[0].name, "Bezimienny")

    def test_list_sorted_by_descending(self):
        mock_sort_by = "-name"
        mock_page_number = 0
        mock_page_size = 10
        sorted_list = self.npc_repository.list(mock_sort_by, mock_page_number, mock_page_size)

        self.assertEqual(sorted_list[0].name, "Xardas")


if __name__ == "__main__":
    unittest.main()
