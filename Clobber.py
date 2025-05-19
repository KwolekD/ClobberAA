from enum import Enum

class Color(Enum):
    CLEAR = 0
    WHITE = 1
    BLACK = 2

class Player:
    def __init__(self, color: Color):
        self.color: Color = color
        self.heuristic = None
        self.pieces = 0

class Clobber:
    def __init__(self,width: int = 5, height: int = 6):
        self.width = width
        self.height = height
        self.board =  [[Color.CLEAR for _ in range(self.width)] for _ in range(self.height)]

    def setPlayers(self,player1: Player, player2: Player):
        if (player1.color == player2.color):
            raise ValueError("Players must have different colors!")
        self.player1 = player1 if player1.color == Color.WHITE else player2
        self.player2 = player2 if player1.color == Color.WHITE else player1
        self._setUpBoard()

    def _setUpBoard(self):
        # Set up the board with player pieces
        if (self.player1 == None or self.player2 == None):
            raise ValueError("Players must be set before setting up the board!")
        for i in range(self.height):
            for j in range(self.width):
                if (j+i) %2 ==0:
                    self.board[i][j] = Color.WHITE
                    self.player1.pieces += 1
                else:
                    self.board[i][j] = Color.BLACK
                    self.player2.pieces += 1

    def __str__(self) -> str:
        board_str: str = ""
        for row in self.board:
            board_str += " | ".join(["_" if cell.value == 0 else "W" if cell.value == 1 else "B" for cell in row]) + "\n"
        return board_str


    




