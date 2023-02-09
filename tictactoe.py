"""
Tic Tac Toe Player
"""

from copy import deepcopy

X = "X"
O = "O"
EMPTY = None

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
    """
    empties = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                empties += 1
    
    if empties % 2 == 0:
        return O
    return X


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
    if player(board) == O:
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
    # Determine who the winner is
    winnerNum = (utility(board))
    if not winnerNum:
        return None
    if winnerNum == -1:
        return X
    return O

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) != None

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winState = (check_rows(board) or
                check_columns(board) or
                check_diagonals(board))
    if winState:
        # If O has won, return -1; else, return 1
        if player(board) == X:
            return -1
        return 1
    # Nobody has won
    return 0

def max_value(board):
    deepBoy = deepcopy(board)
    if terminal(deepBoy):
        return (utility(deepBoy), None)
    wantedAction = None
    v = -2
    for action in actions(deepBoy):
        print("Max Action", action)
        queryV = min_value(result(deepBoy, action))[0]
        if queryV > v:
            v = queryV
            wantedAction = action
    return (v, wantedAction)

def min_value(board):
    deepBoy = deepcopy(board)
    if terminal(deepBoy):
        return (utility(deepBoy), None)
    wantedAction = None
    v = 2
    for action in actions(deepBoy):
        print("Min Action", action)
        queryV = max_value(result(deepBoy, action))[0]
        if queryV < v:
            v = queryV
            wantedAction = action
    
    return (v, wantedAction)

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # The Base Case
    freeSpace = True
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] != EMPTY:
                freeSpace = False
                break
    if freeSpace:
        return (1, 1)
    
    # The Real Minimax
    if player(board) == X:
        return max_value(board)[1]
    return min_value(board)[1]
