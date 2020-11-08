from db.run_sql import run_sql
from models.player import Player
from models.game import Game

def save(player):
    sql = "INSERT INTO players(name) VALUES (%s) RETURNING id"
    values = [player.name]
    results = run_sql(sql, values)
    player.id = results[0]['id']
    return player

def select_all():
    players = []
    sql = "SELECT * FROM players"
    results = run_sql(sql)
    for row in results:
        player = (row['name'], row['id'])
        players.append(player)
    return players

def select(id):
    player = None
    sql = "SELECT * FROM player WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        player = Player(result['name'], result['id'])
    return player

def delete_all():
    sql = "DELETE FROM player"
    run_sql(sql)

def games(player):
    games = []
    sql = "SELECT games.* FROM games INNER JOIN tournaments ON games.id = tournaments.game_id WHERE tournament.user_id = %s"
    values = [player.id]
    results = run_sql(sql, values)
    for row in results:
        game = Game(row['date'], row['id'])
        games.append(game)
    return games