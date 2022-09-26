from flask import Flask
from api.weapons import weapons_router
from api.armors import armors_router

app = Flask(__name__)
app.url_map.strict_slashes = False

app.register_blueprint(weapons_router)
app.register_blueprint(armors_router)


if __name__ == "__main__":
    app.run()