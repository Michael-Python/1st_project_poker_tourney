from flask import Flask, render_template, redirect, Blueprint, request
from models.player import Player
import repositories.player_repository as player_repository

players_blueprint = Blueprint("players", __name__)

# sets up the location in the server for where this happens
@players_blueprint.route("/players")
def players():
    players = player_repository.select_all()
    return render_template("players/index.html", players=players)

# makes a specific directory for specific players
@players_blueprint.route("/players/<id>")
def show(id):
    player = player_repository.select(id)
    games = player_repository.games(player)
    return render_template("players/show.html", player=players, games=games)

# NEW 
# GET players/new
@players_blueprint.route("/players/new", methods=['GET'])
def new_player():
    players = player_repository.select_all()
    return render_template("players/new.html", all_players = players)

# add a player
# CREATE
# POST 'players'
@players_blueprint.route("/players", methods=['POST'])
def add_player():
    new_player = request.form['new_player']
    name = player_repository.select(new_player)
    player = Player(name)
    player_repository.save(player)
    return redirect('/players')

# delete a player
@players_blueprint.route("/players/<id>/delete", methods=['POST'])
def delete_player(id):
    player_repository.delete(id)
    return redirect('/players')