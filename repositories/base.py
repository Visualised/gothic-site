import json, uuid
from dataclasses import asdict, replace
from api_errors import ObjectDoesNotExist
from data import (
    DEFAULT_PAGE_NUMBER,
    DEFAULT_PAGE_SIZE,
    MAX_PAGE_SIZE,
)


class AbstractJSONRepository:
    MODEL = None
    SORTED_BY = None

    def __init__(self, json_file_path: str) -> None:
        self._dataclass_list = self.read_from_json(json_file_path)
        self._json_file_path = json_file_path

    @staticmethod
    def clean_data(json_user_data: dict):
        pass

    def read_from_json(self, json_file_path: str):
        try:
            with open(json_file_path, "r", encoding="utf-8") as f:
                temp_data = json.load(f)
                return [self.MODEL(**object) for object in temp_data]
        except (FileNotFoundError):
            return []

    def save_to_json(self):
        with open(self._json_file_path, "w+", encoding="utf-8") as f:
            object_list = [asdict(object) for object in self._dataclass_list]
            json.dump(object_list, f, indent=2)

    def get(self, id: str):
        found_object = [object for object in self._dataclass_list if object.id == id]
        if not found_object:
            raise ObjectDoesNotExist

        return found_object[0]

    def add(self, json_user_data: dict):
        json_user_data["id"] = str(uuid.uuid4())
        self.clean_data(json_user_data)

        self._dataclass_list.append(self.MODEL(**json_user_data))
        self.save_to_json()

    def update(self, id, json_user_data: dict):
        self.clean_data(json_user_data)
        old_object = self.get(id)
        old_object_index = self._dataclass_list.index(old_object)

        self._dataclass_list[old_object_index] = self.MODEL(**json_user_data, id=old_object.id)
        self.save_to_json()

    def delete(self, id: str):
        self.get(id)

        self._dataclass_list = [i for i in self._dataclass_list if i.id != id]
        self.save_to_json()

    def list(self, sort_by: str, page: int, page_size: int):

        if sort_by[0] == "-":
            is_reversed = True
            sort_by = sort_by[1:]
        else:
            is_reversed = False

        if page < 0:
            page = DEFAULT_PAGE_NUMBER

        if page_size <= 0:
            page_size = DEFAULT_PAGE_SIZE

        if page_size > MAX_PAGE_SIZE:
            page_size = MAX_PAGE_SIZE

        start = page * page_size
        end = (page + 1) * page_size

        sorted_list = sorted(self._dataclass_list, key=self.SORTED_BY[sort_by], reverse=is_reversed)
        return sorted_list[start:end]
