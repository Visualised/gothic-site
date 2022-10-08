from flask import Flask
from api.weapons import WeaponsAPI
from api.armors import ArmorsAPI
from api_errors import APIError

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.errorhandler(APIError)
def handle_bad_request(e):
    return e.description, e.code


def register_api(API_class, endpoint, url):
    view_func = API_class.as_view(endpoint)
    app.add_url_rule(url, defaults={"id": None}, methods=["GET"], view_func=view_func)
    app.add_url_rule(url, methods=["POST"], view_func=view_func)
    app.add_url_rule(f"{url}/<id>", methods=["GET", "PATCH", "DELETE"], view_func=view_func)


register_api(WeaponsAPI, "weapons_api", "/weapons")
register_api(ArmorsAPI, "armors_api", "/armors")


if __name__ == "__main__":
    app.run()
