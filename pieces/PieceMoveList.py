from pieces.Rook import Rook
from board.Board import Board
from board.Tile import Tile


class PieceMoveList:

    def __init__(self, board):
        self.board = board

    def get_move_list(self, piece, x, y):
        if isinstance(piece, Rook):
            return self._get_rook_list(x, y)

    # Updates the list if the tile is empty, if the tile isn't empty returns False to notify the caller that nothing was added. otherwise returns True
    def _list_update(self, moves, x, y):
        moves.append(self.board.get_tile(x, y))
        return self.board.get_tile(x, y).is_empty()

    def _get_rook_list(self, x, y):
        moves = []
        # While going on the y axis x is constant and y is changing denoted by i
        # Going downwards
        for i in range(y + 1, Board.HEIGHT):
            if not self._list_update(moves, x, i):
                break
        # Going upwards
        for i in range(y - 1, -1, -1):
            if not self._list_update(moves, x, i):
                break

        # While going on the x axis y is constant and x is changing denoted by i
        # Going left
        for i in range(x - 1, -1, -1):
            if not self._list_update(moves, i, y):
                break
        # Going right
        for i in range(x + 1, Board.WIDTH):
            if not self._list_update(moves, i, y):
                break

        return moves

    # todo TEST THIS SHIT
    def _get_bishop_list(self, x, y):
        moves = []

        # We will be taking the min of the coordinates for the number of iterations as we are going in diagonals and we need to make sure not to go out of bounds
        # Top left diagonal
        for i in range(min(x, y)):
            if not self._list_update(moves, x - i - 1, y - i - 1):      # Taking a -1 because moving to our own cell isn't a valid move
                break
        # Bottom left diagonal
        for i in range(min(x, y)):
            if not self._list_update(moves, x - i - 1, y + i + 1):
                break
        # Top right diagonal
        for i in range(min(x, y)):
            if not self._list_update(moves, x + i + 1, y - i - 1):
                break
        # Bottom right diagonal
        for i in range(min(x, y)):
            if not self._list_update(moves, x + i + 1, y + i + 1):
                break

    # todo Test this
    def _get_knight_list(self, x, y):
        moves = []

        # The knight moves in an L shape so we will just calculate all moves possible
        # Right side of possible moves
        if Board.valid_point(x + 1, y - 2):
            self._list_update(moves, x + 1, y - 2)
        if Board.valid_point(x + 2, y - 1):
            self._list_update(moves, x + 2, y - 1)
        if Board.valid_point(x + 2, y + 1):
            self._list_update(moves, x + 2, y + 1)
        if Board.valid_point(x + 1, y + 2):
            self._list_update(moves, x + 1, y + 2)

        # Left side of possible moves
        if Board.valid_point(x - 1, y - 2):
            self._list_update(moves, x - 1, y - 2)
        if Board.valid_point(x - 2, y - 1):
            self._list_update(moves, x - 2, y - 1)
        if Board.valid_point(x - 2, y + 1):
            self._list_update(moves, x - 2, y + 1)
        if Board.valid_point(x - 1, y + 2):
            self._list_update(moves, x - 1, y + 2)

        return moves



# b = Board()
# b.board[1][1] = Tile(1, 1, Rook())
# b.board[1][5] = Tile(5, 1, Rook())
# b.board[2][1] = Tile(1, 2, Rook())
# print(b)
# ls = PieceMoveList(b)
# print(len(ls.get_move_list(b.get_tile(5, 1).piece, 5, 1)))

# x = 1
# y = 4
# for i in range(min(x, y)):
#     print(x - i - 1, y + i + 1)