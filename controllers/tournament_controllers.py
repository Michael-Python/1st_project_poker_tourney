from flask import Flask, Blueprint, render_template, redirect, request
from models.tournament import Tournament

import repositories.tournament_repository as tournament_repository
import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

tournaments_blueprint = Blueprint("tournaments", __name__)

# sets up the location in the server for where this happens
@tournaments_blueprint.route("/tournaments")
def tournaments():
    tournaments = tournaments_repository.select.all()
    return render_template("tournaments", tournaments = tournaments)

#NEW
# sets the place where games can be added
@tournaments_blueprint.route("/tournaments/new", methods=['GET'])
def new_game():
    players = player_repository.select.all()
    games = game_repository.select.all()
    return render_template("tournaments/show", games = games, players = players)

#CREATE
@tournaments_blueprint.route("/tournaments", methods=['POST'])
def create_game():
    player_id = request.form['player_id']
    game_id = request.form['game_id']
    # I need to think on this one, still
    # winner = request.form['winner']
    player = player_repository.select(player_id)
    game = game_repository.select(game_id)

    tournament = Tournament(player, game)
    tournament_repository.save(tournament)
    return redirect('/tournament')


#DELETE
@tournaments_blueprint.route("/tournaments/<id>/delete", methods=['POST'])
def delete_game(id):
    tournament_repository.delete(id)
    return redirect('/tounaments')