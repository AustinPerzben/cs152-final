#!/usr/bin/python
#
# 4-in-a-row version of Tic Tac Toe two-player game
# author: Austin Perzben
# created: 2021-04-30


def EvalFunc1(game):
    """
    Straight-forward evaluation function based simply 
    on the game being lost at the current state or not.
    """
    return - 100 if game.lose() else 0


def EvalFunc2(game):
    """
    More specific evaluation function based on how many lines
    exist where the current player has an advantage. Advantage
    here means being the only player with marks on the line in question.

    A better evaluation function for Tic-Tac-Toe is:
        +100 for EACH 3-in-a-line for computer.
        +10 for EACH 2-in-a-line (with a empty cell) for computer.
        +1 for EACH 1-in-a-line (with two empty cells) for computer.
        Negative scores for opponent, i.e., -100, -10, -1 for EACH opponent's 3-in-a-line, 2-in-a-line and 1-in-a-line.
        0 otherwise (empty lines or lines with both computer's and opponent's seed).
    Compute the scores for each of the 8 lines (3 rows, 3 columns and 2 diagonals) and obtain the sum.
    """
    score = 0
    rows = [game.board[i*4:i*4+4] for i in range(4)]
    cols = [game.board[i::4] for i in range(4)]
    diag = [game.board[0::5], game.board[3:13:3]]
    lines = rows + cols + diag
    for line in lines:
        x_taken = sum([1 for x in line if x == game.nplayer])
        x_lost = sum([1 for x in line if x == game.nopponent])
        x_free = sum([1 for x in line if x == 0])
        # print(line)
        # print(x_taken)
        # print(x_free)

        if x_lost == 1 and x_free == 3:
            score -= 1
        elif x_lost == 2 and x_free == 2:
            score -= 10
        elif x_lost == 3 and x_free == 1:
            score -= 100
        if x_taken == 1 and x_free == 3:
            score += 1
        elif x_taken == 2 and x_free == 2:
            score += 10
        elif x_taken == 3 and x_free == 1:
            score += 100
        else:
            score = 0
            break

    return score
