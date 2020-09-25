from typing import Tuple


class Board:
    def clear_board(self):
        return [[self.empty_cell] * self.size for i in range(self.size)]

    def __init__(self, size, empty_cell: str = '.'):
        self.size = size
        self.empty_cell = empty_cell
        self.board = self.clear_board()

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(f"{self.board[i][j]:3}", end="")
            print()

    def set_step(self, symbol: str, pos: Tuple):
        self.board[pos[0]][pos[1]] = symbol

    def is_cell_empty(self, pos: tuple) -> bool:
        return self.board[pos[0]][pos[1]] == self.empty_cell

    def is_valid_cell(self, pos: tuple) -> bool:
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def can_choose_this_cell(self, pos: tuple) -> bool:
        return self.is_valid_cell(pos) and self.is_cell_empty(pos)

    # board = Board(5)
# board.print_board()
# board.set_step('X', (3, 3))
# board.print_board()
