from flask import Flask
from api.npc import NPCAPI
from api.weapons import WeaponsAPI
from api.armors import ArmorsAPI
from api_errors import APIError
from controllers.npc_controller import NPCController
from repositories.armors import JSONArmorsRepository
from repositories.weapons import JSONWeaponsRepository
from repositories.npc import JSONNPCRepository
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


if __name__ == "__main__":
    weapons_repository = JSONWeaponsRepository(WEAPONS_REPOSITORY_JSON_PATH)
    armors_repository = JSONArmorsRepository(ARMORS_REPOSITORY_JSON_PATH)
    npc_repository = JSONNPCRepository(NPC_REPOSITORY_FILE_PATH)
    npc_controller = NPCController(npc_repository, weapons_repository, armors_repository)
    app = create_app(weapons_repository, armors_repository, npc_controller)
    app.run()
