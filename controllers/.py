from flask import Flask, render_template, redirect, Blueprint, request
from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# sets up the location in the server for where this happens
@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players = players)

# makes a specific directory for specific players
@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repository.select(id)
    games = player_repository.players(player)
    return render_template("players/show.html", player = players, games = games)

# add game

# delete game