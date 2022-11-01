from dataclasses import dataclass
from models.base import db


@dataclass
class NPCDBModel(db.Model):
    __tablename__ = "npcs"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, nullable=False)
    hp: int = db.Column(db.Integer, nullable=False)
    mana: int = db.Column(db.Integer, nullable=False)
    guild: str = db.Column(db.String, nullable=False)
    weapon_id: int = db.Column(db.Integer, db.ForeignKey("weapons.id"))
    armor_id: int = db.Column(db.Integer, db.ForeignKey("armors.id"))
