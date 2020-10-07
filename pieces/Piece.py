"""
This class serves as the base blueprint for all other pieces
For the sake of simplicity we call a pawn by the name piece as well
"""

from abc import ABC, abstractmethod
from typing import List
from board.Tile import Tile


class Piece(ABC):

    def __init__(self, alliance, x, y):
        super().__init__()
        self.alliance = alliance
        self.x = x
        self.y = y

    @abstractmethod
    def __repr__(self) -> str:
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def valid_move_list(self, board) -> List[Tile]:
        pass


