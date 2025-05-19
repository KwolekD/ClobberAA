from Clobber import Clobber, Player
from Color import Color

game = Clobber()

player1 = Player(Color.BLACK)
player2 = Player(Color.WHITE)
game.setPlayers(player1, player2)
print(game)