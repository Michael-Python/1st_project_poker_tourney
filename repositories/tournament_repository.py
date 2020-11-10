from db.run_sql import run_sql
from models.player import Player
from models.game import Game

import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

#create
def save(tournament):
    sql = "INSERT INTO tournaments ( game_id, winner, loser) VALUES (%s, %s, %s) RETURNING id "
    values = [tournament.game.id, tournament.winner.id, tournament.loser.id]
    results = run_sql(sql, values)
    tournament.id = results[0]['id']
    return tournament

#read
def select_all():
    tournaments = []

    sql = "SELECT * FROM tournaments"
    results = run_sql(sql)
    
    for row in results:
        game = game_repository.select(row['game_id'])
        winner = player_repository.select(row['game_winner'])
        loser = player_repository.select(row['game_loser'])
        tournament = Tournament(game, winner, loser, row['id'])
        tournaments.append(tournament)
    return tournaments


#update

#delete
def delete_all():
    sql = "DELETE FROM tournaments"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tournaments WHERE id = %s"
    values = [id]
    run_sql(sql, values)