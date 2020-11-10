from flask import Flask, render_template, redirect, request
from flask import Blueprint
from models.game import Game
import repositories.game_repository as game_repository 
import repositories.player_repository as player_repository

games_blueprint = Blueprint("games", __name__)

# sets up the location in the server for where this happens
@games_blueprint.route("/games")
def games():
    games = game_repository.select_all()
    return render_template("games/index.html", games=games)

# makes a specific directory for specific games
@games_blueprint.route("/games/<id>")
def show(id):
    game = game_repository.select(id)
    players = game_repository.players(game)
    return render_template("games/show.html", games=games, players=players)

# NEW 
# GET games/new
@games_blueprint.route("/games/new", methods=['GET'])
def new_game():
    players = player_repository.select_all()
    games = game_repository.select_all()
    return render_template("games/new.html", players = players, all_games = games, )

# add a game
# CREATE
# POST 'games'
@games_blueprint.route("/games", methods=['POST'])
def add_player():
    new_player1 = request.form['player1']
    new_player2 = request.form['player2']
    new_game = request.form['game_number']
    player1 = player_repository.select(new_player1)
    player2 = player_repository.select(new_player2)
    number = game_repository.select(new_game)
    game = Game(player1, player2, number)
    game_repository.save(game)
    return redirect('/games')

# delete a player
@games_blueprint.route("/games/<id>/delete", methods=['POST'])
def delete_game(id):
    game_repository.delete(id)
    return redirect('/games')