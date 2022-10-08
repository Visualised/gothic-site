from flask import Flask
from api.weapons import weapons_router
from api.armors import armors_router
from api_errors import APIError

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(APIError)
def handle_bad_request(e):
    return e.description, e.code


app.register_blueprint(weapons_router)
app.register_blueprint(armors_router)


if __name__ == "__main__":
    app.run()
