import random

from PlayerBase import *


class ComputerPlayer(PlayerBase):

    def __init__(self, name: str, symbol: str, board: Board):
        PlayerBase.__init__(self, name, symbol, board)

    def get_random_pos(self) -> tuple:
        max_rand = self.bord.size - 1
        return random.randint(0, max_rand), random.randint(0, max_rand)

    def next_step(self) -> Tuple:
        pos = self.get_random_pos()
        while not self.bord.can_choose_this_cell(pos):
            pos = self.get_random_pos()
        return pos

# cp = ComputerPlayer("my omputer Player", '0')
# print(cp.next_step())
