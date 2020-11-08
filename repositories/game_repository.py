from db.run_sql import run_sql
from models.player import Player
from models.game import Game

def save(game):
    sql = "INSERT INTO games(date) VALUES (%s) RETURNING id"
    values = [game.date]
    results = run_sql( sql, values )
    game.id = results[0][id]
    return game

def select_all():
    games = []

    sql = "SELECT * FROM games"
    results = run_sql(sql)

    for row in results:
        game = Game(row['date'], row['id'])
        games.append(game)
    return games

def select(id):
    game = None
    sql = "SELECT * FROM games where id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        game = Game(result['date'], result['id'])
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
    return players
