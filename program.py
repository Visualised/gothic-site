from flask import Flask, request

app = Flask(__name__)

@app.route("/swords")
def print_sword_list():
    return sword_list

@app.route("/swords/<int:id>")
def print_sword_details(id):
    if 0 > id or id > (len(sword_list) - 1):
        return "Your ID is out of range"
    sword = sword_list[id]
    return sword

sword_list = [
    {
    "id": 0,
    "name": "Zardzewiały miecz", 
    "damage": 10, 
    "required_strength": 5,
    },
    {
    "id": 1,
    "name": "Miecz Świstaka", 
    "damage": 20, 
    "required_strength": 15,
    },
    {
    "id": 2,
    "name": "Miecz strachu", 
    "damage": 42, 
    "required_strength": 18,
    },
    {
    "id": 3,
    "name": "Miecz śmierci", 
    "damage": 48, 
    "required_strength": 21,
    },
    {
    "id": 4,
    "name": "Miecz Blizny", 
    "damage": 85, 
    "required_strength": 70,
    },
]