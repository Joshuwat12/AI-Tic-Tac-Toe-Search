"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
turn_player = False

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player_flip(player):
    """
    Flips the binary turn_player variable
    """
    turn_player = not turn_player


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    return (not turn_player)


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    # Generate all possible moves
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return utility(board) != 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    return player_num(winner(board))


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
