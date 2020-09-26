import itertools

from ComputerPlayer import *
from GameLogic import *
from HumanPlayer import *


class TheGame:

    def __init__(self, game_logic: GameLogic, players: List[PlayerBase], bord: Board):
        self.game_logic = game_logic
        self.players = self.players = itertools.cycle(players)
        self.bord = bord

    def next_player(self) -> PlayerBase:
        return next(self.players)

    def start_game(self):
        game_end = False
        current_player = ""
        while not game_end:
            current_player = self.next_player()
            print(f"{current_player.name} playing ... ")
            self.bord.print_board()
            step = current_player.next_step()
            self.bord.set_step(current_player.symbol, step)
            game_end = self.game_logic.is_win(current_player.symbol)
        print(f"----- Player {current_player.name} Win !!! ")


board = Board(3)
game_logic = GameLogic(board)
hp = HumanPlayer("Amiel", 'X', board)
cp = ComputerPlayer("My Computer", '0', board)
players = [hp, cp]

the_game = TheGame(game_logic, players, board)
the_game.start_game()
