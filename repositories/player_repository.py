from db.run_sql import run_sql
from models.player import Player
from models.game import Game
import repositories.game_repository as game_repository

def save(player):
    sql = "INSERT INTO players(name) VALUES (%s) RETURNING id"
    values = [player.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    player.id = id
    return player

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = Player(row['name'], row['id'])
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM players WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        # game = game_repository.select(result['game'])
        player = Player(result['name'], result['id'])
    return player

def delete_all():
    sql = "DELETE FROM players"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM players WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def games(player):
    games = []
    sql = "SELECT games.* FROM games INNER JOIN players ON (games.player1 = players.id OR games.player2 = players.id) WHERE players.id = %s"
    values = [player.id]
    results = run_sql(sql, values)
    for row in results:
        game = Game(row['number'], row['player1'], row['player2'], row['id'])
        games.append(game)
    return games