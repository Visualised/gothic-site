from flask import Flask
from flask_migrate import Migrate
from api.npc import NPCAPI
from api.weapons import WeaponsAPI
from api.armors import ArmorsAPI
from api.locations import LocationsAPI
from api.enemies import EnemiesAPI
from api_errors import APIError
from controllers.npc_controller import NPCController
from controllers.weapons_controller import WeaponsController
from controllers.armors_controller import ArmorsController
from controllers.locations_controllers import LocationsController
from controllers.enemies_controller import EnemiesController
from repositories.armors import DBArmorsRepository
from repositories.weapons import DBWeaponsRepository
from repositories.npc import DBNPCRepository
from repositories.locations import DBLocationsRepository
from repositories.enemies import DBEnemiesRepository
from models.base import db


def register_api(API_class, endpoint, url, app, repository):
    view_func = API_class.as_view(endpoint, repository)
    app.add_url_rule(url, defaults={"id": None}, methods=["GET"], view_func=view_func)
    app.add_url_rule(url, methods=["POST"], view_func=view_func)
    app.add_url_rule(f"{url}/<id>", methods=["GET", "PATCH", "DELETE"], view_func=view_func)


def create_app(weapons_repository, armors_repository, npc_controller, locations_controller, enemies_controller, testing: bool = False):
    app = Flask(__name__)
    app.testing = testing
    app.url_map.strict_slashes = False
    register_api(WeaponsAPI, "weapons_api", "/weapons", app, weapons_repository)
    register_api(ArmorsAPI, "armors_api", "/armors", app, armors_repository)
    register_api(NPCAPI, "npc_api", "/npc", app, npc_controller)
    register_api(LocationsAPI, "locations_api", "/locations", app, locations_controller)
    register_api(EnemiesAPI, "enemies_api", "/enemies", app, enemies_controller)

    @app.errorhandler(APIError)
    def handle_bad_request(e):
        return e.description, e.code

    return app


weapons_db_repository = DBWeaponsRepository()
weapons_controller = WeaponsController(weapons_db_repository)
armors_db_repository = DBArmorsRepository()
armors_controller = ArmorsController(armors_db_repository)
npc_db_repository = DBNPCRepository()
npc_controller = NPCController(npc_db_repository, weapons_db_repository, armors_db_repository)
locations_db_repository = DBLocationsRepository()
locations_controller = LocationsController(locations_db_repository)
enemies_db_repository = DBEnemiesRepository()
enemies_controller = EnemiesController(enemies_db_repository)
app = create_app(weapons_controller, armors_controller, npc_controller, locations_controller, enemies_controller)

app.config.from_object("config")

db.init_app(app)
migrate = Migrate(app, db)
