class LocationsController:
    def __init__(self, locations_repository) -> None:
        self.locations_repository = locations_repository

    def get(self, id: str):
        return self.locations_repository.get(id)

    def list(self, sort_by: str, page: int, page_size: int):
        return self.locations_repository.list(sort_by, page, page_size)

    def add(self, json_user_data: dict):
        return self.locations_repository.add(json_user_data)

    def update(self, id: str, json_user_data: dict):
        return self.locations_repository.update(id, json_user_data)

    def delete(self, id: str):
        return self.locations_repository.delete(id)
