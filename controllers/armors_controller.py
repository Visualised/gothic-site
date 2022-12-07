from dataclasses import asdict


class ArmorsController:
    def __init__(self, armors_repository) -> None:
        self.armors_repository = armors_repository

    def get(self, id: str):
        return asdict(self.armors_repository.get(id))

    def list(self, sort_by: str, page: int, page_size: int):
        return self.armors_repository.list(sort_by, page, page_size)

    def add(self, json_user_data: dict):
        return self.armors_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        return self.armors_repository.update(id, json_user_data)

    def delete(self, id: str):
        return self.armors_repository.delete(id)
