from application.data.database import db
from application.data.model import Game as game_model
from flask import jsonify
from flask_restful import Resource, fields, marshal, marshal_with, reqparse

# ? id, title, genre, played
game_fields = {
    'id': fields.Integer,
    'title': fields.String,
    'genre': fields.String,
    'played': fields.Boolean
}

games_parser = reqparse.RequestParser()
games_parser.add_argument(
    'id', type=int, help="id is optional !")
games_parser.add_argument(
    'title', type=str, required=True, help="Title is required !")
games_parser.add_argument(
    'genre', type=str, required=True, help="Genre is required !")
games_parser.add_argument(
    'played', type=bool, help="played can be given optionally !")


class GameResource(Resource):
    # ? to send all the games
    # @marshal_with(game_fields)
    def get(self):
        games = game_model.query.all()
        # return jsonify({"status": 'success', 'games': games})
        return jsonify({'status': 'success', 'games': marshal(games, game_fields)})

    def post(self):
        args = games_parser.parse_args()
        title = args.get('title')
        if not title:
            return jsonify({"status": 'failure', 'message': 'game title is required !'}), 400
        genre = args.get('genre')

        new_game = game_model(title=title, genre=genre)
        db.session.add(new_game)
        db.session.commit()
        return jsonify({"status": 'success', 'message': 'game is added !'})

    def put(self):
        print('here !')
        args = games_parser.parse_args()
        id = args.get('id')
        game = game_model.query.filter_by(id=id).first()
        if not game:
            return jsonify({"status": 'failure', 'message': 'game not found !'}), 404
        title = args.get('title')
        # if not title:
        #     return jsonify({"status": 'failure', 'message': 'game title is required !'}), 400
        genre = args.get('genre')
        played = args.get('played')
        if not played:
            played = False
        game.title = title
        game.genre = genre
        game.played = played
        db.session.commit()
        return jsonify({"status": 'success', 'message': 'game is updated !'})

    def delete(self):
        pass


class SingleGameResource(Resource):
    # ? to send all the games
    # @marshal_with(game_fields)
    def get(self, gameid):
        games = game_model.query.filter_by(id=gameid).first()
        # return jsonify({"status": 'success', 'games': games})
        return jsonify({'status': 'success', 'game': marshal(games, game_fields)})
