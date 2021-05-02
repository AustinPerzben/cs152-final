#!/usr/bin/python
#
# 4-in-a-row version of Tic Tac Toe two-player game
# author: Austin Perzben
# created: 2021-04-30

from copy import deepcopy
from players import RealPlayer, AIPlayer
from evaluation_functions import EvalFunc1, EvalFunc2


class TTTPlus:
    """ The board positions are numbered as follows:
             1  2  3  4
             5  6  7  8
             9 10 11 12
            13 14 15 16

    """

    def __init__(self, players):
        self.players = players
        self.board = [0 for i in range(16)]
        self.nplayer = 1  # player 1 starts.

    def play(self, nmoves=1000, verbose=True):
        """
        Method for starting the play of a game to completion.
        -----------
        nmoves:
          The limit of how many moves (plies) to play unless the game ends on
          it's own first.
        verbose:
          Setting verbose=True displays additional text messages.
        """

        history = []

        if verbose:
            self.show()

        for self.nmove in range(1, nmoves + 1):

            if self.is_over():
                break

            move = self.player.ask_move(self)
            history.append((deepcopy(self), move))
            self.make_move(move)
            # print(f'board: {self.board}')1

            if verbose:
                print("\nMove #%d: player %d plays %s :" % (
                      self.nmove, self.nplayer, str(move)))
                self.show()

            self.switch_player()

        history.append(deepcopy(self))

        return history

    @property
    def nopponent(self):
        return 2 if (self.nplayer == 1) else 1

    @property
    def player(self):
        return self.players[self.nplayer - 1]

    @property
    def opponent(self):
        return self.players[self.nopponent - 1]

    def possible_moves(self):
        return [i+1 for i, e in enumerate(self.board) if e == 0]

    def make_move(self, move):
        self.board[int(move)-1] = self.nplayer

    def switch_player(self):
        self.nplayer = self.nopponent

    def copy(self):
        return deepcopy(self)

    def get_move(self):
        """
        Method for getting a move from the current player.
        """
        return self.player.ask_move(self)

    def play_move(self, move):
        """
        Method for playing one move with the current player.
        -----------
        move:
          The move to be played; should match an entry in the '.possibles_moves()' list.
        """
        result = self.make_move(move)
        self.switch_player()
        return result

    def lose(self):
        """ Does the opponent have four in a row? """
        lose_lines = [[1, 2, 3, 4], [5, 6, 7, 8],
                      [9, 10, 11, 12], [13, 14, 15, 16],  # hor
                      [1, 5, 9, 13], [2, 6, 10, 14],
                      [3, 7, 11, 15], [4, 8, 12, 16],  # ver
                      [1, 6, 11, 16], [4, 7, 10, 13]]  # diag
        for line in lose_lines:
            for c in line:
                if all([(self.board[c-1] == self.nopponent) for c in line]):
                    return True
        return False

    def is_over(self):
        return (self.possible_moves() == []) or self.lose()

    def show(self):
        print('\n'+'\n'.join([
            ' '.join([['.', 'O', 'X'][self.board[4*j+i]]
                      for i in range(4)])
            for j in range(4)]))


if __name__ == "__main__":
    eval_func = EvalFunc2
    TTTPlus([AIPlayer(eval_func, max_depth=6), RealPlayer()]).play()
