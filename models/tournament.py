class Tournament:
    def __init__(self, player1_id, player2_id, game_id, winner, loser, id = None):
        self.player1_id = player1_id
        self.player2_id = player2_id
        self.game_id = game_id
        self.winner = winner
        self.loser = loser
        self.id = id