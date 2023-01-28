from dataclasses import dataclass
from models.base import db


@dataclass
class EnemiesDBModel(db.Model):
    __tablename__ = "enemies"

    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String, unique=True, nullable=False)