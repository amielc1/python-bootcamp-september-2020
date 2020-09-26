from PlayerBase import *

BoardPosition = Tuple[int, int]


class HumanPlayer(PlayerBase):
    def __init__(self, name: str, symbol: str, board: Board):
        super().__init__(name, symbol, board)

    def get_cell_from_user(self) -> BoardPosition:
        user_input = input("please enter your next step (row,col)")
        try:
            pos = [int(i) for i in user_input.split(',')]
            return pos
        except Exception:
            raise Exception("Please enter a valid position format")

    def next_step(self) -> BoardPosition:
        pos = self.get_cell_from_user()
        while not self.bord.can_choose_this_cell(pos):
            pos = self.get_cell_from_user()
        return pos
