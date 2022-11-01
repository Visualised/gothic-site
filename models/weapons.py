from dataclasses import dataclass
from models.base import db


@dataclass
class WeaponDBModel(db.Model):
    __tablename__ = "weapons"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, unique=True, nullable=False)
    damage: int = db.Column(db.Integer, nullable=False)
    required_strength: int = db.Column(db.Integer, nullable=False)
    required_dexterity: int = db.Column(db.Integer, nullable=False)
    type: str = db.Column(db.String, nullable=False)
    npcs = db.relationship("NPCDBModel", backref="weapons")
