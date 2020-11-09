class Tournament:
    def __init__(self, game_id, winner, loser, id = None):
        self.game_id = game_id
        self.winner = winner
        self.loser = loser
        self.id = id