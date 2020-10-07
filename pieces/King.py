from pieces.Piece import Piece
from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Bishop import Bishop
from pieces.Knight import Knight
from pieces.Pawn import Pawn


class King(Piece):

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.moved = False

    def __repr__(self):
        return 'K'

    def move(self):
        pass

    # Returns the valid move list for a certain position
    # O(1) Time complexity
    def valid_move_list(self, board):
        cells = []
        if board.valid_point(self.x - 1, self.y - 1):  # Top left
            cells.append(board[self.y - 1][self.x - 1])
        if board.valid_point(self.x, self.y - 1):  # Top
            cells.append(board[self.y - 1][self.x])
        if board.valid_point(self.x + 1, self.y - 1):  # Top right
            cells.append(board[self.y - 1][self.x + 1])
        if board.valid_point(self.x - 1, self.y):  # Left
            cells.append(board[self.y][self.x - 1])
        if board.valid_point(self.x + 1, self.y):  # Right
            cells.append(board[self.y][self.x + 1])
        if board.valid_point(self.x - 1, self.y + 1):  # Bottom left
            cells.append(board[self.y + 1][self.x - 1])
        if board.valid_point(self.x, self.y + 1):  # Bottom
            cells.append(board[self.y + 1][self.x])
        if board.valid_point(self.x + 1, self.y + 1):  # Bottom Right
            cells.append(board[self.y + 1][self.x + 1])
        return cells

    def is_checked(self, board) -> bool:
        # Looking for checking pieces in column or row
        for tile in Rook(self.alliance, self.x, self.y).valid_move_list(board):
            if isinstance(tile.piece, Rook) and tile.piece.alliance != self.alliance:
                return True
            if isinstance(tile.piece, Queen) and tile.piece.alliance != self.alliance:
                return True

        # Looking for checking pieces in diagonals
        for tile in Bishop(self.alliance, self.x, self.y).valid_move_list(board):
            if isinstance(tile.piece, Bishop) and tile.piece.alliance != self.alliance:
                return True
            if isinstance(tile.piece, Queen) and tile.piece.alliance != self.alliance:
                return True

        # Looking for checking knights
        for tile in Knight(self.alliance, self.x, self.y).valid_move_list(board):
            if isinstance(tile.piece, Knight) and tile.piece.alliance != self.alliance:
                return True

        # Looking for checking pawns
        if board.valid_point(self.x - 1, self.y - 1):
            if isinstance(board[self.y - 1][self.x - 1].piece, Pawn):
                return True
        if board.valid_point(self.x + 1, self.y - 1):
            if isinstance(board.valid_point(self.x + 1, self.y - 1), Pawn):
                return True

        return False



