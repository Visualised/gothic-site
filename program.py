from flask import Flask, request
from http import HTTPStatus
import uuid

app = Flask(__name__)

@app.route("/swords")
def print_sword_list():
    return sword_list, HTTPStatus.OK

@app.route("/swords", methods=["POST"])
def add_sword():
    json_data = request.get_json()
    json_data["id"] = uuid.uuid4()
    sword_list.append(json_data)
    return "Sword has been added", HTTPStatus.CREATED

@app.route("/swords/<id>")
def print_sword_details(id):
    sword = filter_by_id(id, sword_list)
    if not sword:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND
    return sword[0], HTTPStatus.OK

@app.route("/swords/<id>", methods=["DELETE"])
def delete_sword(id):
    global sword_list
    sword = filter_by_id(id, sword_list)
    if not sword:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND
    sword_list = [i for i in sword_list if i["id"] != id]
    return f'Sword {sword[0]["name"]} has been deleted.', HTTPStatus.OK

@app.route("/swords/<id>", methods=["PATCH"])
def update_sword(id):
    sword = filter_by_id(id, sword_list)
    if not sword:
        return "This ID doesn't exist", HTTPStatus.NOT_FOUND
    json_data = request.get_json()
    sword[0].update(json_data)
    return "Sword has been updated", HTTPStatus.OK
    
def filter_by_id(id, sequence):
    return list(filter(lambda sword: sword["id"] == id, sequence))


sword_list = [
    {
    "id": "P4nKuuuurtk4-z-nwidii-k000x",
    "name": "Zardzewiały miecz", 
    "damage": 10, 
    "required_strength": 5,
    },
    {
    "id": "Jaa444-ni3-chc3-tyl3-z4r4bi4c",
    "name": "Miecz Świstaka", 
    "damage": 20, 
    "required_strength": 15,
    },
    {
    "id": "pies3k-szcz3sl1wy",
    "name": "Miecz strachu", 
    "damage": 42, 
    "required_strength": 18,
    },
    {
    "id": "eeeeeeeeeeeeeeeeeeee",
    "name": "Miecz śmierci", 
    "damage": 48, 
    "required_strength": 21,
    },
    {
    "id": "j3st-d0w0d-n4-t0-ajdi",
    "name": "Miecz Blizny", 
    "damage": 85, 
    "required_strength": 70,
    },
]

if __name__ == "__main__":
    app.run()