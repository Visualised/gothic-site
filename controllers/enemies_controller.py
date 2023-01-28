from dataclasses import asdict


class EnemiesController:
    def __init__(self, enemies_repository) -> None:
        self.enemies_repository = enemies_repository

    def get(self, id: str):
        return asdict(self.enemies_repository.get(id))

    def list(self, sort_by: str, page: int, page_size: int):
        return self.enemies_repository.list(sort_by, page, page_size)

    def add(self, json_user_data: dict):
        return self.enemies_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        return self.enemies_repository.update(id, json_user_data)

    def delete(self, id: str):
        return self.enemies_repository.delete(id)
