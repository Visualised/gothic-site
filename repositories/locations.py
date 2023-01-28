from repositories.base import AbstractDBRepository
from models.locations import LocationDBModel

class DBLocationsRepository(AbstractDBRepository):
    DB_MODEL = LocationDBModel
    ORDER_BY = {
        "id": LocationDBModel.id,
        "name": LocationDBModel.name,
    }

    def get(self, object_id: int):
        db_query_result = self.DB_MODEL.query.get(object_id)

        return {
            "id": db_query_result.id,
            "name": db_query_result.name,
            "enemy_types": db_query_result.enemy_types,
        }
