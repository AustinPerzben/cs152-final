#!/usr/bin/python
#
# 4-in-a-row version of Tic Tac Toe two-player game
# author: Austin Perzben
# created: 2021-04-30

# Python3 program to demonstrate
# working of Alpha-Beta Pruning
# Initial values of Aplha and Beta
from evaluation_functions import EvalFunc1, EvalFunc2


class RealPlayer():
    def __init__(self, name='Human Player'):
        self.name = name

    def ask_move(self, game):
        possible_moves = game.possible_moves()
        # The str version of every move for comparison with the user input:
        possible_moves_str = list(map(str, game.possible_moves()))
        move = "NO_MOVE_DECIDED_YET"
        while True:
            move = input("\nPlayer %s what do you play ? " % (game.nplayer))
            if move == 'show moves':
                print("Possible moves:\n" + "\n".join(
                    ["#%d: %s" % (i+1, m) for i, m in enumerate(possible_moves)])
                    + "\nType a move or type 'move #move_number' to play.")

            elif move == 'quit':
                raise KeyboardInterrupt

            elif move.startswith("move #"):
                # Fetch the corresponding move and return.
                move = possible_moves[int(move[6:])-1]
                return move

            elif str(move) in possible_moves_str:
                # Transform the move into its real type (integer, etc. and return).
                move = possible_moves[possible_moves_str.index(str(move))]
                return move

    def __str__(self):
        return self.name


class AIPlayer():
    def __init__(self, eval_func, max_depth=9, name='AI Player'):
        self.name = name
        self.move = {}
        self.eval = eval_func
        self.depth = max_depth

    def negamax(self, game, depth, og_depth, alpha=float('-infinity'), beta=float('infinity')):

        # Terminating condition. i.e
        # leaf node is reached
        if depth == 0 or game.is_over():
            score = self.eval(game)
            if score == 0:
                return score
            else:
                return (score - 0.01*depth*abs(score)/score)
            # print(f'score {score}')
            return score

        possible_moves = game.possible_moves()
        # print(f'moves {possible_moves}')
        state = game
        best_move = possible_moves[0]

        if depth == og_depth:
            state.ai_move = possible_moves[0]

        bestValue = float('-infinity')

        # Recur for left and right children
        for move in possible_moves:

            game = state.copy()  # re-initialize move

            game.make_move(move)
            game.switch_player()

            move_alpha = -self.negamax(game, depth-1, og_depth, -beta, -alpha)

            if bestValue < move_alpha:
                bestValue = move_alpha
                best_move = move

            if alpha < move_alpha:
                alpha = move_alpha
                if depth == og_depth:
                    state.ai_move = move
                if (alpha >= beta):
                    break
        return bestValue

    def ask_move(self, game):
        self.alpha = self.negamax(game, self.depth, self.depth)
        return game.ai_move

    def __str__(self):
        return self.name
