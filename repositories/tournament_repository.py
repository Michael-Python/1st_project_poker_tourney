from db.run_sql import run_sql
from models.player import Player
from models.game import Game

import repositories.game_repository as game_repository
import repositories.player_repository as player_repository

#create
def save(tournament):
    sql = "INSERT INTO tournaments ( player_id, game_id) VALUES (%s, %s) RETURNING id "
    values = [tournament.player_id, tournament.game_id]
    results = run_sql(sql, values)
    tournament.id = results[0]['id']
    return tournament

#read
def select_all():
    tournaments = []

    sql = "SELECT * FROM tournaments"
    results = run_sql(sql)
    
    for row in results:
        player = player_repository.select(row['player_id'])
        game = game_repository.select(row['game_id'])
        tournament = Tournament(player, game, row['id'])
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