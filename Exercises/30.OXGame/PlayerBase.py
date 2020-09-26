from Board import *

BoardPosition = Tuple[int, int]


class PlayerBase:
    def __init__(self, name: str, symbol: str, bord: Board):
        self.name = name
        self.symbol = symbol
        self.bord = bord

    def next_step(self) -> BoardPosition:
        pass
