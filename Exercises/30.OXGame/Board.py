from typing import Tuple


class Board:
    # You usually want to write __init__ as the first method in the class
    def __init__(self, size, empty_cell: str = '.'):
        self.size = size
        self.empty_cell = empty_cell
        self.board = self.clear_board()

    def clear_board(self):
        # Cool. Can you guess what would happen if you did this instead?
        # d=[['.'] * 3] * 3
        return [[self.empty_cell] * self.size for i in range(self.size)]

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(f"{self.board[i][j]:3}", end="")
            print()

    def set_step(self, symbol: str, pos: Tuple):
        # A type hint can (should) be more specific Tuple[int,int]
        # Also I'd implement a small helper function to get/set the cell by its position
        # and just write here:
        # self.set_cell(pos, symbol)
        self.board[pos[0]][pos[1]] = symbol

    def is_cell_empty(self, pos: tuple) -> bool:
        # and here:
        # return self.cell(pos) == self.empty_cell
        return self.board[pos[0]][pos[1]] == self.empty_cell

    def is_valid_cell(self, pos: tuple) -> bool:
        return 0 <= pos[0] < self.size and 0 <= pos[1] < self.size

    def can_choose_this_cell(self, pos: tuple) -> bool:
        return self.is_valid_cell(pos) and self.is_cell_empty(pos)

    # board = Board(5)
# board.print_board()
# board.set_step('X', (3, 3))
# board.print_board()
