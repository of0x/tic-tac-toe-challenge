from tictactoe import app

from flask import jsonify, request
from flask import json


from tictactoe.models import Game
from tictactoe.datatbase import db_session
from tictactoe.error_handlers import InvalidUsage


# @app.route('/api/games', endpoint='games', methods=['GET','POST'])
# @app.route('/', methods=['GET','POST'])
@app.route('/api/games', methods=['GET','POST'])
def index():

    if request.method == 'POST':
        request_json = request.get_json()
        game = Game()
        if request_json is not None:
            if 'firstPlayer' in request_json:
                game.firstPlayer = request_json['firstPlayer']
            if 'secondPlayer' in request_json:
                game.secondPlayer = request_json['secondPlayer']
            if 'board' in request_json:
                game.board = request_json['board']
        db_session.add(game)
        db_session.commit()
        return jsonify(construct_dict(game))
    else:
        response = []
        for game in Game.query.all():
            response.append(construct_dict(game))
        return json.dumps(response)


@app.route('/api/games/<int:game_id>', methods=['GET', 'POST', 'DELETE'])
def game(game_id):
    game = Game.query.filter(Game.id == game_id).first()
    if game is None:
        raise InvalidUsage('Game id:' + str(game_id) + ' is not found', 404)
    if request.method == 'POST':
        request_json = request.get_json()
        if request_json is not None:
            if 'firstPlayer' in request_json:
                game.firstPlayer = request_json['firstPlayer']
            if 'secondPlayer' in request_json:
                game.secondPlayer = request_json['secondPlayer']
            if 'board' in request_json:
                game.board = request_json['board']
        db_session.commit()
    elif request.method == 'DELETE':
        db_session.delete(game)
        db_session.commit()
        return jsonify(dict())
    if game:
        return jsonify(construct_dict(game))
    else:
        return jsonify(dict())


@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def construct_dict(game):
    return dict(id=game.id, firstPlayer=game.firstPlayer,
                secondPlayer=game.secondPlayer, board=game.board)




@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()