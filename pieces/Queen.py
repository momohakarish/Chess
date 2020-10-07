from pieces.Piece import Piece
from pieces.Bishop import Bishop
from pieces.Rook import Rook


class Queen(Piece):
    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def __repr__(self):
        return 'Q'

    def move(self):
        pass

    # The queens valid moves can be calculated as the valid moves of a rook and a bishop combined
    def valid_move_list(self, board):
        return Rook(self.alliance, self.x, self.y).valid_move_list(board) + Bishop(self.alliance, self.x, self.y).valid_move_list(board)


