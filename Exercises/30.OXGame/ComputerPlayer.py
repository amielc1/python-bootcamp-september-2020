import random

from PlayerBase import *
from typing import Tuple

# Note how you have Tuple[int, int] as a position
# everywhere in your code... 
# For such cases it's useful to define a custom type variable:

BoardPosition = Tuple[int, int]

# Even better would be to import this variable from some common file
# so everyone will have the same type defs

# Now you can use BoardPosition as a type hint everywhere you wrote Tuple

class ComputerPlayer(PlayerBase):

    def __init__(self, name: str, symbol: str, board: Board):
        # Better to use super:
        # super().__init__(name, symbol, board)
        PlayerBase.__init__(self, name, symbol, board)

    def get_random_pos(self) -> BoardPosition:
        max_rand = self.bord.size - 1
        # No need to convert randint() to int - it's already an int
        return (random.randint(0, max_rand), random.randint(0, max_rand))

    def next_step(self) -> BoardPosition:
        # A better structure is the while True loop,
        # because now you only need to write the get_random_pos call once
        while True:
            pos = self.get_random_pos()
            if self.bord.can_choose_this_cell(pos):
                return pos

# cp = ComputerPlayer("my omputer Player", '0')
# print(cp.next_step())
