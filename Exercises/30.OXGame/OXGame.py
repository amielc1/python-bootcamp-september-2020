import collections


class BoardUtils:
    def perform_on_board(self, board, code_to_run_for_each_item):
        for i in range(len(board)):
            for j in range(len(board[i])):
                res = code_to_run_for_each_item(i, j, j == len(board[i]) - 1)
                if res is not None:
                    return res

    def print_board(self, board):
        self.perform_on_board(
            board,
            lambda i, j, is_last: print(
                f"{board[i][j]:3}", end="\n" if is_last else ""
            ),
        )


class Score:
    def __init__(self):
        self.score = collections.defaultdict(int)

    def game_over(self, win, name):
        if win:
            self.score[name] += 10


class BasePlayer:
    def __init__(self, score_keeper):
        self.score = score_keeper

    def game_over(self, win):
        self.score.game_over(win, self.name)


class HumanPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        print(self.score)
        self.name = "HumanPlayer"

    def next_move(self, board):
        BoardUtils().print_board(board)
        next_move = input("What's your next move? type the square position as (row, column)")
        print(next_move)
        return next_move


class AIPlayer(BasePlayer):
    def __init__(self, score_keeper):
        super().__init__(score_keeper)
        self.name = "Bot"

    def next_move(self, board):
        def foreach_cell(i, j, is_last):
            if board[i][j] == '.':
                return f"({j}, {i})"

        utils = BoardUtils()
        return utils.perform_on_board(
            board,
            foreach_cell,
        )


#
score_keeper = Score()
h = HumanPlayer(score_keeper)
a = AIPlayer(score_keeper)
board = [['x', '.', '.'], ['o', '.', '.'], ['.', '.', '.']]
while True:
    h.next_move(board)
    res = a.next_move(board)
    print(res)
#
# a.game_over(True)
# a.game_over(True)
# h.game_over(True)
#
# print(h.score.score)
