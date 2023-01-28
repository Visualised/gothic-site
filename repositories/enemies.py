from repositories.base import AbstractDBRepository
from models.enemies import EnemiesDBModel 

class DBEnemiesRepository(AbstractDBRepository):
    DB_MODEL = EnemiesDBModel
    ORDER_BY = {
        "id": EnemiesDBModel.id,
        "name": EnemiesDBModel.name,
    }