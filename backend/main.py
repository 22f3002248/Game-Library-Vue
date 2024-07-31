import uuid

from application.api.game_api import GameResource, SingleGameResource
from application.data.database import db
from config import devconfig
from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api

# from flask_security import Security

app = Flask(__name__)

app.config.from_object(devconfig)

CORS(app, resources={r"/*": {"origins": "*"}})


db.init_app(app)
api = Api(app)
api.init_app(app)
# app.security = Security(app, ds)
with app.app_context():
    db.create_all()


@app.route("/", methods=["GET"])
@app.route("/sharkcomp", methods=["GET"])
def shark():
    return "Shark in ~ S E A ~"


GAMES = [
    {
        "id": uuid.uuid4().hex,
        "title": "The Elder Scrolls V: Skyrim",
        "genre": "RPG",
        "played": True,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Grand Theft Auto V",
        "genre": "Action",
        "played": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "The Witcher 3: Wild Hunt",
        "genre": "Fantasy",
        "played": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "World of Warcraft",
        "genre": "MMORPG",
        "played": True,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Civilization VI",
        "genre": "Strategy",
        "played": True,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Settlers of Catan",
        "genre": "Board",
        "played": False,
    },
    {
        "id": uuid.uuid4().hex,
        "title": "Tetris Effect",
        "genre": "Puzzle",
        "played": False,
    },
]


@app.route("/", methods=["GET", "POST"])
@app.route("/games", methods=["GET", "POST"])
def all_games():
    response = {"status": "success"}
    if request.method == "POST":
        data = request.get_json()
        GAMES.append(
            {
                "id": uuid.uuid4().hex,
                "title": data.get("title"),
                "genre": data.get("genre"),
                "played": data.get("played"),
            }
        )
        response["message"] = "game added"
    else:
        response["games"] = GAMES
    return jsonify(response)


@app.route("/game/<game_id>", methods=["PUT", "DELETE"])
def game_op(game_id):
    """
    Perform operations on a game based on the HTTP method used.
    If the method is PUT, update the game details with the provided data.
    If the method is DELETE, remove the game.
    Parameters:
    - game_id: str, the unique identifier of the game to operate on
    Returns:
    - JSON response indicating the status and message of the operation
    """
    response = {"status": "success"}
    if request.method == "PUT":
        data = request.get_json()
        remove_game(game_id)
        GAMES.append(
            {
                "id": uuid.uuid4().hex,
                "title": data.get("title"),
                "genre": data.get("genre"),
                "played": data.get("played"),
            }
        )
        response["message"] = "game updated"
    elif request.method == "DELETE":
        remove_game(game_id)
        response["message"] = "game deleted"
    return jsonify(response)


def remove_game(id):
    for GAME in GAMES:
        if GAME["id"] == id:
            GAMES.remove(GAME)
            return True
    return False


# > http://127.0.0.1:5000/api/game
api.add_resource(GameResource, '/api/games')

# > http://127.0.0.1:5000/api/game/1
api.add_resource(SingleGameResource, '/api/game/<int:gameid>')
if __name__ == "__main__":
    app.run(debug=True)
