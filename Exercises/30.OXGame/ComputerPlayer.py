import random

from PlayerBase import *

BoardPosition = Tuple[int, int]


class ComputerPlayer(PlayerBase):

    def __init__(self, name: str, symbol: str, board: Board):
        super().__init__(name, symbol, board)

    def get_random_pos(self) -> BoardPosition:
        max_rand = self.bord.size - 1
        return random.randint(0, max_rand), random.randint(0, max_rand)

    def next_step(self) -> BoardPosition:
        pos = self.get_random_pos()
        while not self.bord.can_choose_this_cell(pos):
            pos = self.get_random_pos()
        return pos
