import uuid, json

json_file_path = "data/armors.json"

class JSONArmorsRepository:
    def __init__(self, json_file_path) -> None:
        self._json_in_memory = self.read_from_json(json_file_path)
        self._json_file_path = json_file_path

    def read_from_json(self, json_file_path):
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    def save_to_json(self, json_file_path):
        with open(json_file_path, "w+", encoding="utf-8") as f:
            json.dump(self._json_in_memory, f, indent=2)

    def list(self):
        return self._json_in_memory

    def get(self, id):
        armor = list(filter(lambda x: x["id"] == id, self._json_in_memory))
        return armor[0] if armor else None

    def add(self, json_user_data):
        json_user_data["id"] = str(uuid.uuid4())

        self._json_in_memory.append(json_user_data)
        self.save_to_json(self._json_file_path)
        return True

    def update(self, id, json_user_data):
        armor = self.get(id)
        if not armor:
            return False
        
        armor.update(json_user_data)
        self.save_to_json(self._json_file_path)
        return True

    def delete(self, id):
        armor = self.get(id)
        if not armor:
            return False

        self._json_in_memory = [i for i in self._json_in_memory if i["id"] != id]
        self.save_to_json(self._json_file_path)
        return True

class InMemoryArmorsRepository:

    def __init__(self, armors_list) -> None:
        self._armors_list = armors_list
        
    def list(self):
        return self._armors_list

    def get(self, id):
        armor = list(filter(lambda x: x["id"] == id, self._armors_list))
        return armor[0] if armor else None

    def add(self, json_user_data):
        json_user_data["id"] = str(uuid.uuid4())
        self._armors_list.append(json_user_data)
        return True

    def update(self, id, json_data):
        armor = self.get(id)
        if not armor or not self.verify_type(json_data):
            return False

        armor.update(json_data) 
        return True

    def delete(self, id):
        armor = self.get(id)
        if not armor:
            return False

        self._armors_list = [i for i in self._armors_list if i["id"] != id]
        return True

armors_repository = JSONArmorsRepository(json_file_path)