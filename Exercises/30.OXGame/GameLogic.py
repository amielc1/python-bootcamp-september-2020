from typing import List
from Board import *


class GameLogic:

    def __init__(self, board: Board):
        self.board = board

    def is_win(self, sym: str) -> bool:
        for i in range(self.board.size):
            if self.is_same(self.board.get_row(i), sym) or self.is_same(self.board.get_col(i), sym):
                return True
        if self.is_same(self.board.get_r_diagonal(), sym) or self.is_same(self.board.get_l_diagonal(), sym):
            return True
        return False

    def is_same(self, lst: List, sym: str) -> bool:
        return len(set(lst)) == 1 and lst[0] == sym
