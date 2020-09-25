from typing import Tuple

import numpy as np


class Board:
    def clear_board(self):
        return np.full((self.size, self.size), self.empty_cell)

    def __init__(self, size, empty_cell: str = '.'):
        self.size = size
        self.empty_cell = empty_cell
        self.board = self.clear_board()

    def print_board(self):
        print(self.board)

    def set_step(self, symbol: str, pos: Tuple):
        self.board[pos[0], pos[1]] = symbol

    def is_cell_empty(self, pos: tuple) -> bool:
        return self.board[pos[0], pos[1]] == self.empty_cell

    def is_valid_cell(self, pos: tuple) -> bool:
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def can_choose_this_cell(self, pos: tuple) -> bool:
        return self.is_valid_cell(pos) and self.is_cell_empty(pos)

    def get_row(self, i):
        return self.board[i]

    def get_col(self, i):
        return self.board[:, i]

    def get_r_diagonal(self):
        diag = ([0, 1, 2], [0, 1, 2])
        return self.board[diag]

    def get_l_diagonal(self):
        diag = ([0, 1, 2], [2, 1, 0])
        return self.board[diag]
