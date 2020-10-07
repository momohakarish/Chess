"""
This class represents the rook piece
"""
from typing import List
from board.Tile import Tile
from pieces.Piece import Piece


class Rook(Piece):

    def __init__(self, alliance, x, y):
        super().__init__(alliance, x, y)
        moved = False

    def __repr__(self):
        return 'R'

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

    def valid_move_list(self, board) -> List[Tile]:
        moves = []
        alliance = self.alliance

        # While going on the y axis x is constant and y is changing denoted by i
        # Going downwards
        for i in range(self.y + 1, board.get_height()):
            if not self.__list_update(moves, self.x, i, board, alliance):
                break
        # Going upwards
        for i in range(self.y - 1, -1, -1):
            if not self.__list_update(moves, self.x, i, board, alliance):
                break

        # While going on the x axis y is constant and x is changing denoted by i
        # Going left
        for i in range(self.x - 1, -1, -1):
            if not self.__list_update(moves, i, self.y, board, alliance):
                break
        # Going right
        for i in range(self.x + 1, board.get_width()):
            if not self.__list_update(moves, i, self.y, board, alliance):
                break

        return moves

