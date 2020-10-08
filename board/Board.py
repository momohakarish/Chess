"""
This class represents a chess board
"""

from typing import List
from board.Tile import Tile
from pieces.Bishop import Bishop
from pieces.King import King
from pieces.Pawn import Pawn
from pieces.Queen import Queen
from pieces.Rook import Rook
from pieces.Knight import Knight


class Board:

    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.board = [[Tile(i, j) for j in range(Board.WIDTH)] for i in range(Board.HEIGHT)]

    def __repr__(self) -> str:
        board = ''
        for row in self.board:
            board += str(row) + '\n'
        return board

    def __getitem__(self, index: int) -> List[Tile]:
        return self.board[index]

    # Filling the board with the pieces in their starting positions
    def fill(self):
        # Rooks
        self.board[0][0].piece = Rook('Black', 0, 0)
        self.board[0][7].piece = Rook('Black', 0, 7)
        self.board[7][0].piece = Rook('White', 7, 0)
        self.board[7][7].piece = Rook('White', 7, 7)

        # Knights
        self.board[0][1].piece = Knight('Black', 0, 1)
        self.board[0][6].piece = Knight('Black', 0, 6)
        self.board[7][1].piece = Knight('White', 7, 1)
        self.board[7][6].piece = Knight('White', 7, 6)

        # Bishops
        self.board[0][2].piece = Bishop('Black', 0, 2)
        self.board[0][5].piece = Bishop('Black', 0, 5)
        self.board[7][2].piece = Bishop('White', 7, 2)
        self.board[7][5].piece = Bishop('White', 7, 5)

        # Queens
        self.board[0][3].piece = Queen('Black', 0, 3)
        self.board[7][3].piece = Queen('White', 7, 3)

        # Kings
        self.board[0][4].piece = King('Black', 0, 4)
        self.board[7][4].piece = King('White', 7, 4)

        # Pawns
        for pawn in range(Board.WIDTH):
            self.board[1][pawn].piece = Pawn('Black', pawn, 1)
            self.board[6][pawn].piece = Pawn('White', pawn, 6)

    # Returns the width of the board
    @classmethod
    def get_width(cls) -> int:
        return cls.WIDTH

    # Returns the height of the board
    @classmethod
    def get_height(cls) -> int:
        return cls.HEIGHT

    # Checks if a point in the matrix is valid
    # O(1) Time complexity
    # O(1) Space complexity
    @staticmethod
    def valid_point(x: int, y: int) -> bool:
        return Board.WIDTH > x >= 0 and Board.HEIGHT > y >= 0

