from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.game import Game
import repositories.game_repository as game_repository 

games_blueprint = Blueprint("games", __name__)

# sets up the location in the server for where this happens
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html")

# makes a specific directory for specific games
@games_blueprint.route("/games/<id>")
def show(id):
    game = game_repository.select(id)
    players = game_repository.players(game)
    return render_template("games/show.html", game=games, players=players)