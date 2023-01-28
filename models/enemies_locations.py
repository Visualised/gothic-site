from models.base import db
from dataclasses import dataclass


@dataclass
class EnemyLocationDBModel(db.Model):
    tablename = "enemies_locations"

    id: int = db.Column(db.Integer, primary_key=True)
    enemy_id: int = db.Column(db.Integer, db.ForeignKey('enemies.id'))
    location_id: int = db.Column(db.Integer, db.ForeignKey('locations.id'))