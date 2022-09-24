from data import weapons_list, WeaponType
import uuid

class InMemoryWeaponsRepository:

    def __init__(self, weapons_list) -> None:
        self._weapons_list = weapons_list

    def verify_type(self, json_data):
        try:
            WeaponType(json_data["type"])
            return True
        except ValueError:
            return False

    def list(self):
        return self._weapons_list

    def get(self, id):
        weapon = list(filter(lambda x: x["id"] == id, self._weapons_list))
        return weapon[0] if weapon else None

    def add(self, json_data):
        json_data["id"] = uuid.uuid4()
        if self.verify_type(json_data):
            self._weapons_list.append(json_data)
            return True

        return False

    def update(self, id, json_data):
        weapon = self.get(id)
        if not weapon or not self.verify_type(json_data):
            return False

        weapon.update(json_data) 
        return True

    def delete(self, id):
        weapon = self.get(id)
        if not weapon:
            return False

        self._weapons_list = [i for i in self._weapons_list if i["id"] != id]
        return True

weapons_repository = InMemoryWeaponsRepository(weapons_list)