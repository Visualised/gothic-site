import unittest
from unittest.mock import Mock, patch
from api_errors import ObjectDoesNotExist
from app import create_app
from repositories.weapons import JSONWeaponsRepository
from repositories.armors import JSONArmorsRepository
from dataclasses import asdict

JSON_FILE_PATH_WEAPONS = "tests/fixtures/test_weapons_data.json"
JSON_FILE_PATH_ARMORS = "tests/fixtures/test_armors_data.json"


class Test_WeaponsRouter(unittest.TestCase):
    def setUp(self):
        self.test_weapons_repository = JSONWeaponsRepository(JSON_FILE_PATH_WEAPONS)
        self.app = create_app(self.test_weapons_repository, None, None, testing=True)
        self.app_tester = self.app.test_client()
        self.mock_json_user_data = {
            "name": "Wielki Mjeczyk",
            "damage": 77,
            "required_strength": 33,
            "required_dexterity": 9,
            "type": "sword",
        }

    def test_print_weapon_list(self):
        parameters = {
            "sort_by": "damage",
            "page": 1,
            "page_size": 2,
        }
        response = self.app_tester.get("/weapons", query_string=parameters)
        sorted_dataclass_list = self.test_weapons_repository.list(**parameters)
        self.assertEqual(response.get_json(), [asdict(obj) for obj in sorted_dataclass_list])

    def test_print_weapon_details(self):
        weapon_id = "6501ksdu-usta-4079-8b74-760cbc575b45"
        response = self.app_tester.get(f"/weapons/{weapon_id}", query_string=weapon_id)
        self.assertDictEqual(response.get_json(), asdict(self.test_weapons_repository.get(weapon_id)))

    @patch("repositories.weapons.JSONWeaponsRepository.save_to_json")
    def test_add_weapon(self, mock_save_to_json: Mock):
        dataclass_list_before_add = self.test_weapons_repository._dataclass_list.copy()
        self.test_weapons_repository.add(self.mock_json_user_data)
        dataclass_list_after_add = self.test_weapons_repository._dataclass_list.copy()

        self.assertNotEqual(dataclass_list_before_add, dataclass_list_after_add)
        mock_save_to_json.assert_called_once()

    @patch("repositories.weapons.JSONWeaponsRepository.save_to_json")
    def test_update_weapon(self, mock_save_to_json: Mock):
        weapon_id = "6501ksdu-usta-4079-8b74-760cbc575b45"
        weapon_before_patch = self.test_weapons_repository.get(weapon_id)

        self.test_weapons_repository.update(weapon_id, self.mock_json_user_data)
        weapon_after_patch = self.test_weapons_repository.get(weapon_id)

        self.assertNotEqual(weapon_before_patch, weapon_after_patch)
        mock_save_to_json.assert_called_once()

    @patch("repositories.weapons.JSONWeaponsRepository.save_to_json")
    def test_delete_weapon(self, mock_save_to_json: Mock):
        weapon_id = "6501ksdu-usta-4079-8b74-760cbc575b45"

        self.test_weapons_repository.delete(weapon_id)
        with self.assertRaises(ObjectDoesNotExist):
            self.test_weapons_repository.get(weapon_id)

        mock_save_to_json.assert_called_once()


class Test_ArmorsRouter(unittest.TestCase):
    def setUp(self):
        self.test_armors_repository = JSONArmorsRepository(JSON_FILE_PATH_ARMORS)
        self.app = create_app(None, self.test_armors_repository, None, testing=True)
        self.app_tester = self.app.test_client()
        self.mock_json_user_data = {
            "name": "ffffffMega Armor",
            "weapon_resistance": 300,
            "ranged_resistance": 350,
            "fire_resistance": 400,
            "magic_resistance": 450,
            "price": 1000,
        }

    def test_print_armor_list(self):
        parameters = {
            "sort_by": "-name",
            "page": 1,
            "page_size": 2,
        }
        response = self.app_tester.get("/armors", query_string=parameters)
        sorted_dataclass_list = self.test_armors_repository.list(**parameters)
        self.assertEqual(response.get_json(), [asdict(obj) for obj in sorted_dataclass_list])

    def test_print_armor_details(self):
        armor_id = "345cc691-b59f-4860-8ba0-418b9ae8a672"
        response = self.app_tester.get(f"/armors/{armor_id}", query_string=armor_id)
        self.assertDictEqual(response.get_json(), asdict(self.test_armors_repository.get(armor_id)))

    @patch("repositories.armors.JSONArmorsRepository.save_to_json")
    def test_add_armor(self, mock_save_to_json: Mock):
        dataclass_list_before_add = self.test_armors_repository._dataclass_list.copy()
        self.test_armors_repository.add(self.mock_json_user_data)
        dataclass_list_after_add = self.test_armors_repository._dataclass_list.copy()

        self.assertNotEqual(dataclass_list_before_add, dataclass_list_after_add)
        mock_save_to_json.assert_called_once()

    @patch("repositories.armors.JSONArmorsRepository.save_to_json")
    def test_update_armor(self, mock_save_to_json: Mock):
        armor_id = "345cc691-b59f-4860-8ba0-418b9ae8a672"
        armor_before_patch = self.test_armors_repository.get(armor_id)

        self.test_armors_repository.update(armor_id, self.mock_json_user_data)
        armor_after_patch = self.test_armors_repository.get(armor_id)

        self.assertNotEqual(armor_before_patch, armor_after_patch)
        mock_save_to_json.assert_called_once()

    @patch("repositories.armors.JSONArmorsRepository.save_to_json")
    def test_delete_armor(self, mock_save_to_json: Mock):
        armor_id = "345cc691-b59f-4860-8ba0-418b9ae8a672"

        self.test_armors_repository.delete(armor_id)
        with self.assertRaises(ObjectDoesNotExist):
            self.test_armors_repository.get(armor_id)

        mock_save_to_json.assert_called_once()


if __name__ == "__main__":
    unittest.main()
