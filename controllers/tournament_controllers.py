from flask import Flask, Blueprint, render_template, redirect, request
from models.tournament import Tournament

import repositories.tournament_repository as tournament_repository
import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

tournaments_blueprint = Blueprint("tournaments", __name__)

# sets up the location in the server for where this happens
@tournaments_blueprint.route("/tournaments")
def tournaments():
    tournaments = tournament_repository.select_all()
    return render_template("tournaments/index.html", tournaments=tournaments)

#NEW
# # sets the place where games can be added
# @tournaments_blueprint.route("/tournaments/new", methods=['GET'])
# def update_tournament():
#     games = game_repository.select_all()
#     return render_template("tournaments/new.html", tournaments=tournaments)

#CREATE
@tournaments_blueprint.route("/tournaments", methods=['POST'])
def create_game():
    game_id_name = request.form['game_number']
    winner_name = request.form['winner']
    loser_name = request.form['loser']
    game_id = game_repository.select(game_id_name)
    winner = player_repository.select(winner_name)
    loser = player_repository.select(loser_name)
    tournament = Tournament(game_id, winner, loser)
    tournament_repository.save(tournament)
    return redirect('/tournaments')


#DELETE
@tournaments_blueprint.route("/tournaments/<id>/delete", methods=['POST'])
def delete_game(id):
    tournament_repository.delete(id)
    return redirect('/tounaments')