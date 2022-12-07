from flask import Flask
from flask_migrate import Migrate
from api.npc import NPCAPI
from api.weapons import WeaponsAPI
from api.armors import ArmorsAPI
from api_errors import APIError
from controllers.npc_controller import NPCController
from controllers.weapons_controller import WeaponsController
from controllers.armors_controller import ArmorsController
from repositories.armors import JSONArmorsRepository, DBArmorsRepository
from repositories.weapons import JSONWeaponsRepository, DBWeaponsRepository
from repositories.npc import JSONNPCRepository, DBNPCRepository
from models.base import db
from models.weapons import WeaponDBModel
from data import (
    WEAPONS_REPOSITORY_JSON_PATH,
    ARMORS_REPOSITORY_JSON_PATH,
    NPC_REPOSITORY_FILE_PATH,
)


def register_api(API_class, endpoint, url, app, repository):
    view_func = API_class.as_view(endpoint, repository)
    app.add_url_rule(url, defaults={"id": None}, methods=["GET"], view_func=view_func)
    app.add_url_rule(url, methods=["POST"], view_func=view_func)
    app.add_url_rule(f"{url}/<id>", methods=["GET", "PATCH", "DELETE"], view_func=view_func)


def create_app(weapons_repository, armors_repository, npc_controller, testing: bool = False):
    app = Flask(__name__)
    app.testing = testing
    app.url_map.strict_slashes = False
    register_api(WeaponsAPI, "weapons_api", "/weapons", app, weapons_repository)
    register_api(ArmorsAPI, "armors_api", "/armors", app, armors_repository)
    register_api(NPCAPI, "npc_api", "/npc", app, npc_controller)

    @app.errorhandler(APIError)
    def handle_bad_request(e):
        return e.description, e.code

    return app


# if __name__ == "__main__":
# weapons_repository = JSONWeaponsRepository(WEAPONS_REPOSITORY_JSON_PATH)
weapons_db_repository = DBWeaponsRepository()
weapons_controller = WeaponsController(weapons_db_repository)
# armors_repository = JSONArmorsRepository(ARMORS_REPOSITORY_JSON_PATH)
armors_db_repository = DBArmorsRepository()
armors_controller = ArmorsController(armors_db_repository)
# npc_repository = JSONNPCRepository(NPC_REPOSITORY_FILE_PATH)
npc_db_repository = DBNPCRepository()
npc_controller = NPCController(npc_db_repository, weapons_db_repository, armors_db_repository)
app = create_app(weapons_controller, armors_controller, npc_controller)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
migrate = Migrate(app, db)
# app.run()
