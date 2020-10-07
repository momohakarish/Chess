from pieces.Piece import Piece


class Knight(Piece):

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)

    def __repr__(self):
        return 'N'

    def move(self):
        pass

    def valid_move_list(self, board):
        moves = []

        # The knight moves in an L shape so we will just calculate all moves possible
        # Adding all possible moves and then removing all tiles which have the knights allied pieces
        # Right side of possible moves
        if board.valid_point(self.x + 1, self.y - 2):
            moves.append(board[self.y - 2][self.x + 1])
        if board.valid_point(self.x + 2, self.y - 1):
            moves.append(board[self.y - 1][self.x + 2])
        if board.valid_point(self.x + 2, self.y + 1):
            moves.append(board[self.y + 1][self.x + 2])
        if board.valid_point(self.x + 1, self.y + 2):
            moves.append(board[self.y + 2][self.x + 1])

        # Left side of possible moves
        if board.valid_point(self.x - 1, self.y - 2):
            moves.append(board[self.y - 2][self.x - 1])
        if board.valid_point(self.x - 2, self.y - 1):
            moves.append(board[self.y - 1][self.x - 2])
        if board.valid_point(self.x - 2, self.y + 1):
            moves.append(board[self.y + 1][self.x - 2])
        if board.valid_point(self.x - 1, self.y + 2):
            moves.append(board[self.y + 2][self.x - 1])

        # Removing tiles containing allied pieces
        for tile in moves:
            if not tile.is_empty():
                if tile.piece.alliance == self.alliance:
                    moves.remove(tile)

        return moves

