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
    global turn_player
    turn_player = not turn_player


def player():
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
    global turn_player
    if turn_player:
        board[action[0]][action[1]] = O
    else:
        board[action[0]][action[1]] = X
    return board


def constant(l):
    """
    Returns True if all items in the list are the same and not EMPTY,
    else False otherwise.
    """
    for value in l:
        if value == EMPTY or value != l[0]:
            return False
    return True

def check_diagonals(board):
    """
    Returns True if the diagonals are the same and not EMPTY,
    else returns False.
    """
    if center == EMPTY:
        return False
    center = board[1][1]
    if check_diagonals_helper(board, 0, 2, center):
        return True
    elif check_diagonals_helper(board, 2, 0, center):
        return True
    return False

def check_diagonals_helper(board, x, y, center):
    """
    Helper function for check diagonals. Returns true if the diagonals
    are the same and not empty, else returns False.
    """
    if board[x][0] == center:
            if board[y][2] == center:
                return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #Checks the rows
    for row in range(len(board)):
        if constant(board[row]):
            return board[row][0]
    #Checks the columns
    for col in range(len(board[0])):
        if constant([n[col] for n in board]):
            return board[0][col]
    
    #Checks the diagonals
    winState = check_diagonals(board)
    #TODO: Check if winState
    #TODO: Return which player, if either, wins



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return utility(board) != 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    p = winner(board)
    if p == "X":
        return 1
    if p == "O":
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
