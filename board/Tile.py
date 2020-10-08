"""
This class represents a tile in a chess board
"""


class Tile:

    def __init__(self, x, y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece      # If tile is empty then the piece is None

    def __repr__(self) -> str:
        if self.piece is None:
            return '0'
        else:
            return str(self.piece)

    # Implementing __eq__ and __hash__ so we can create a set of tiles in other parts of the program
    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))

    def is_empty(self) -> bool:
        return self.piece is None

    def reset(self):
        self.piece = None


