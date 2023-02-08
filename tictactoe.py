"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
global turnPlayer
turnPlayer = False

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    False is X's turn; True is O's turn.
    """
    global turnPlayer
    return turnPlayer


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    # Generate all possible moves
    for i in range(len(board)):
        for j in range(len(board[i])):
            # Append all viable moves as tuples
            if board[i][j] == EMPTY:
                actions.append((i, j))
    return actions

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # If turn_player is True, it is O's turn, else it is X's.
    print(turnPlayer, action)
    if action == None:
        return board
    if turnPlayer:
        board[action[0]][action[1]] = O
    else:
        board[action[0]][action[1]] = X
    return board


def constant(checkList):
    """
    Returns True if all items in the list are the same and not EMPTY,
    else returns False.
    """
    # We proceed by assuming the list items are the same and not EMPTY
    for value in checkList:
        # Check for contradiction
        if value == EMPTY or value != checkList[0]:
            return False
    return True

def check_rows(board):
    """
    Returns True if all items in any row are the same and not EMPTY,
    else returns False.
    """
    # Iterate through each row
    for row in board:
        if constant(row):
            return True
    # No winning row
    return False

def check_columns(board):
    """
    Returns True if all items in any column are the same and not EMPTY,
    else returns False.
    """
    # Iterate through each column
    for colNum in range(len(board)):
        # Build columns with array generation
        column = [row[colNum] for row in board]
        if constant(column):
            return True
    # No winning column
    return False

def check_diagonals(board):
    """
    Returns True if the diagonals are the same and not EMPTY,
    else returns False.
    """
    # Establish the center of the board
    center = board[1][1]
    if center == EMPTY:
        return False
    # Check the diagonals
    if check_diagonals_helper(board, 0, 2, center):
        return True
    elif check_diagonals_helper(board, 2, 0, center):
        return True
    # No winning diagonal
    return False

def check_diagonals_helper(board, x, y, center):
    """
    Helper function for check_diagonals. Returns true if the diagonals
    are the same and not empty, else returns False.
    """
    # Compare the diagonals to the center
    if board[x][0] == center:
            if board[y][2] == center:
                return True
    return False

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check if there is a winner
    winState = (check_rows(board) or
                check_columns(board) or
                check_diagonals(board))
    # Determine who the winner is
    winnerNum = (utility(board, winState))
    if not winnerNum:
        return None
    if winnerNum == -1:
        return O
    return X


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None

def utility(board, winState):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winState:
        # If O has won, return -1; else, return 1
        if turnPlayer:
            return -1
        else:
            return 1
    # Nobody has won
    return 0

def minimax_bandage(x_or_o):
    if x_or_o == X:
        return float(1)
    return float(-1)

def max_value(board):
    if terminal(board):
        return winner(board)
    else:
        value = -math.inf
        for action in actions(board):
            value = max(value,minimax_bandage(min_value(result(board,action))))
        return value

def min_value(board):
    if terminal(board):
        return winner(board)
    else:
        value = math.inf
        for action in actions(board):
            value = min(value,minimax_bandage(max_value(result(board,action))))
        return value 

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        print('why does this exist')
        pass
        #return None
    if True:
        print('this is fun')
        if turnPlayer:
            max_eval = -math.inf

            for action in actions(board):
                next_eval = minimax_bandage(min_value(result(board, action)))
                
                max_eval = max(max_eval, next_eval)
                if max_eval == max_value(board):
                    print('before end action')
                    return action

        else:
            min_eval = math.inf
            for action in actions(board):
                next_eval = minimax_bandage(max_value(result(board, action)))
            
                min_eval = min(min_eval, next_eval)
                if min_eval == min_value(board):
                    print('before end action')
                    return action
            
#Functions max_value, min_value, minimax inspired by what others have done and shared on the internet.
#minimax is attempting to find either the best way for current player, or the least favorable for the other, using the value functions.
#The max() function returns the largest of the input values.
#The min() function returns the smallest of the input values.
# - John