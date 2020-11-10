from db.run_sql import run_sql
from models.player import Player
from models.game import Game
import repositories.player_repository as player_repository

def save(game):
    sql = "INSERT INTO games(number, player1, player2) VALUES (%s, %s, %s) RETURNING id"
    values = [game.number, game.player1.id, game.player2.id]
    results = run_sql( sql, values )
    # ensure all names are aligned across the code, maybe dropdb and createdb to debug
    id = results[0]['id']
    game.id = id
    # return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        # this gives player 1 and 2  a value from the player file
        player1 = player_repository.select(row['player1'])
        player2 = player_repository.select(row['player2'])
        game = Game(row['number'], player1, player2, row['id'])
        games.append(game)
    return games

def select(id):
    game = None
    sql = "SELECT * FROM games where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    print(result[0])
    if result is not None:
        player1 = player_repository.select(result['player1'])
        player2 = player_repository.select(result['player2'])
        game = Game(result['number'], player1, player2, result['id'])
    return result

def delete_all():
    sql = "DELETE FROM games"
    run_sql(sql)

def players(game):
    players = []
    sql = "SELECT players.* FROM players INNER JOIN tournaments ON players.id = tournaments.player_id WHERE tournaments.game_id = %s"
    values = [game.id]
    results = run_sql(sql, values)
    for row in results:
        player = Player(row['name'], row['id'])
        players.append(player)
        
def delete(id):
    sql = "DELETE FROM games WHERE id = %s"
    values = [id]
    run_sql(sql, values)