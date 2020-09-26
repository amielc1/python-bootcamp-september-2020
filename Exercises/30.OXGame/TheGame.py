from typing import List

from Board import *
from ComputerPlayer import *
from GameLogic import *
from HumanPlayer import *


class TheGame:
    # Why is this a static variable???
    step_counter: int = 0

    def __init__(self, game_logic: GameLogic, players: List[PlayerBase], bord: Board):
        self.game_logic = game_logic
        self.players = players
        self.bord = bord
        # itertools has a nice way to implement next player:
        # import itertools
        # self.players = itertools.cycle(players)

    def next_player(self) -> PlayerBase:
        # return next(self.players)
        the_game.step_counter += 1
        return self.players[the_game.step_counter % 2]

    def start_game(self):
        while not self.game_logic.is_win():
            current_player = self.next_player()
            print(f"{current_player.name} playing ... ")
            self.bord.print_board()
            step = current_player.next_step()
            self.bord.set_step(current_player.symbol, step)


game_logic = GameLogic()
board = Board(3)
hp = HumanPlayer("Amiel", 'X', board)
cp = ComputerPlayer("My Computer", '0', board)
players = [hp, cp]

the_game = TheGame(game_logic, players, board)
the_game.start_game()
