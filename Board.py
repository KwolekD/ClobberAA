from Color import Color

class Board:
    def __init__(self, width: int = 5, height: int = 6) -> None:
        self.width = width
        self.height = height
        self.__board = [[Color.CLEAR for _ in range(width)] for _ in range(height)]


    def get(self,x: int, y: int) -> Color:
        if not (0 <= x < self.width and 0 <= y < self.height):
            raise IndexError("Coordinates out of bounds")
        return self.__board[x][y]
    
    def setUp(self) -> None:
        for i in range(self.height):
            for j in range(self.width):
                self.__board[i][j] = Color.WHITE if (j+i) %2 == 0  else self.__board[i][j] = Color.BLACK

    def __str__(self) -> str:
        board_str: str = ""
        for row in self.__board:
            board_str += " | ".join(["_" if cell.value == 0 else "W" if cell.value == 1 else "B" for cell in row]) + "\n"
        return board_str
        
    