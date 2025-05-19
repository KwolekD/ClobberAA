from Color import Color
from Board import Board
class Player:
    def __init__(self, color: Color):
        self.color: Color = color
        self.heuristic = None

class Clobber:
    def __init__(self,width: int = 5, height: int = 6):
        self.width = width
        self.height = height
        self.board =  Board(width,height)

    def setPlayers(self,player1: Player, player2: Player):
        if (player1.color == player2.color):
            raise ValueError("Players must have different colors!")
        
        if (player1.color == Color.CLEAR or player2.color == Color.CLEAR):
            raise ValueError("Player must not have CLEAR color!")
        self.player1 = player1 if player1.color == Color.WHITE else player2
        self.player2 = player2 if player1.color == Color.WHITE else player1
        self._setUpBoard()

    def _setUpBoard(self):
        if (self.player1 == None or self.player2 == None):
            raise ValueError("Players must be set before setting up the board!")
        self.board.setUp()




    




