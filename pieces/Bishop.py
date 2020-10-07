from pieces.Piece import Piece


class Bishop(Piece):

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def __repr__(self):
        return 'B'

    def move(self):
        pass

    # Updates the list if the tile is empty or occupied by an enemy piece, if the tile is occupied returns false. otherwise returns True
    def __list_update(self, moves, x, y, board, alliance) -> bool:
        # Getting the tile
        tile = board[y][x]

        # If the tile is empty return true and append the tile to the list
        if tile.is_empty():
            moves.append(tile)
            return True

        # If the piece is trying to move onto it's own ally piece then that isn't a valid move
        if tile.piece.alliance == alliance:
            return False

        # If the tile is occupied by an enemy piece
        moves.append(board[y][x])
        return False

    def valid_move_list(self, board):
        moves = []

        # We will be taking the min of the coordinates for the number of iterations as we are going in diagonals and we need to make sure not to go out of bounds
        # Top left diagonal
        for i in range(min(self.x, self.y)):
            if not self.__list_update(moves, self.x - i - 1,  self.y - i - 1, board, self.alliance):  # Taking a -1 because moving to our own cell isn't a valid move
                break
        # Bottom left diagonal
        for i in range(min(self.x, self.y)):
            if not self.__list_update(moves, self.x - i - 1, self.y + i + 1, board, self.alliance):
                break
        # Top right diagonal
        for i in range(min(self.x, self.y)):
            if not self.__list_update(moves, self.x + i + 1, self.y - i - 1, board, self.alliance):
                break
        # Bottom right diagonal
        for i in range(min(self.x, self.y)):
            if not self.__list_update(moves, self.x + i + 1, self.y + i + 1, board, self.alliance):
                break

        return moves
