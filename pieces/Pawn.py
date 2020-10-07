from pieces.Piece import Piece


class Pawn(Piece):

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        self.special_move = True

    def __repr__(self):
        return 'P'

    def move(self):
        pass

    def valid_move_list(self, board):
        moves = []
        alliance = board.get_tile(self.x, self.y).piece.alliance

        # If this is the first time the pawn has moved
        # Move cannot be out of bounds as the pawn is in its default position
        if self.special_move:
            if board.get_tile(self.x, self.y - 2).is_empty():
                moves.append(board.get_tile(self.x, self.y - 2))

        # Checking regular movement
        if board.valid_point(self.x, self.y - 1):     # Checking if the pawn is trying to go out of the board
            if board.get_tile(self.x, self.y - 1).is_empty():     # Pawns cannot capture moving straight so the tile has to be empty
                moves.append(board.get_tile(self.x, self.y - 1))

        # Checking for diagonal captures
        # Top left diagonal
        if board.valid_point(self.x - 1, self.y - 1):
            # The pawn can only capture on diagonals so if the diagonal is empty the pawn cannot capture
            if not board.get_tile(self.x - 1, self.y - 1).is_empty() and board.get_tile(self.x - 1, self.y - 1).piece.alliance != alliance:
                moves.append(board.get_tile(self.x - 1, self.y - 1))

        # Top right diagonal
        if board.valid_point(self.x + 1, self.y - 1):
            if not board.get_tile(self.x + 1, self.y - 1).is_empty() and board.get_tile(self.x + 1, self.y - 1).piece.alliance != alliance:
                moves.append(board.get_tile(self.x + 1, self.y - 1))



