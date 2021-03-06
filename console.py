import pdb

from models.game import Game
from models.player import Player
from models.tournament import Tournament

import repositories.game_repository as game_repository
import repositories.player_repository as player_repository
import repositories.tournament_repository as tournament_repository

# Every time console starts, all entries, that were saved, are deleted

tournament_repository.delete_all()
player_repository.delete_all()
game_repository.delete_all()

# starts adding entries
player1 = Player('Charo')
player_repository.save(player1)

player2 = Player('Neil')
player_repository.save(player2)

player3 = Player('Joe')
player_repository.save(player3)

game1 = Game(1, player1, player2)
game_repository.save(game1)

game2 = Game(2, player1, player3)
game_repository.save(game2)

game3 = Game(3, player3, player2)
game_repository.save(game3)

tournament1 = Tournament(game1, player1, player2)
tournament_repository.save(tournament1)

tournament2 = Tournament(game2, player3, player1)
tournament_repository.save(tournament2)

pdb.set_trace()
