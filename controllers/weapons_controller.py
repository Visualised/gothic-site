from dataclasses import asdict


class WeaponsController:
    def __init__(self, weapons_repository) -> None:
        self.weapons_repository = weapons_repository

    def get(self, id: str):
        return asdict(self.weapons_repository.get(id))

    def list(self, sort_by: str, page: int, page_size: int):
        return self.weapons_repository.list(sort_by, page, page_size)

    def add(self, json_user_data: dict):
        return self.weapons_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        return self.weapons_repository.update(id, json_user_data)

    def delete(self, id: str):
        return self.weapons_repository.delete(id)
