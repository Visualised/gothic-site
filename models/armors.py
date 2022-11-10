from dataclasses import dataclass
from models.base import db


@dataclass
class ArmorDBModel(db.Model):
    __tablename__ = "armors"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, unique=True, nullable=False)
    weapon_resistance: int = db.Column(db.Integer, nullable=False)
    ranged_resistance: int = db.Column(db.Integer, nullable=False)
    fire_resistance: int = db.Column(db.Integer, nullable=False)
    magic_resistance: int = db.Column(db.Integer, nullable=False)
    price: int = db.Column(db.Integer, nullable=False)
    npcs = db.relationship("NPCDBModel", backref="armors", lazy=False)
