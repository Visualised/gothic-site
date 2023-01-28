from dataclasses import dataclass
from models.base import db
from models.enemies_locations import EnemyLocationDBModel


@dataclass
class LocationDBModel(db.Model):
    __tablename__ = "locations"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, unique=True, nullable=False)

    @property
    def enemy_types(self):
        return EnemyLocationDBModel.query.filter(EnemyLocationDBModel.location_id == self.id).count()