from data import sword_list
import uuid

class InMemorySwordsRepository:

    def __init__(self, sword_list) -> None:
        self.sword_list = sword_list

    def list(self):
        return self.sword_list

    def get(self, id):
        sword = list(filter(lambda x: x["id"] == id, self.sword_list))
        return sword[0] if sword else None

    def add(self, json_data):
        json_data["id"] = uuid.uuid4()
        self.sword_list.append(json_data)

    def update(self, id, json_data):
        sword = self.get(id)
        if not sword:
            return False
        sword.update(json_data)
        return True

    def delete(self, id):
        sword = self.get(id)
        if not sword:
            return False
        self.sword_list = [i for i in self.sword_list if i["id"] != id]
        return True

swords_repository = InMemorySwordsRepository(sword_list)