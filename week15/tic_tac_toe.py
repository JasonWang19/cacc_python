# Instructions
# Demonstrates programmer-created functions

from week15.functions import answer_question
# import week15.functions as fnc

# global constants
X = "X"
O = "0"
EMPTY = " "
TIE = "TIE"
NUM_SQUARES = 9


def instructions():
    """Display game instructions."""
    print(
        """
        Tic-Tac-Toe.
        
        Need to enter a number, 0 - 8.  The number
        will correspond to the board position as illustrated:
    
                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8
    
        Game start! \n
        """
    )


def ask_number(question, low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


def pieces():
    """Determine if player or computer goes first."""
    go_first = answer_question("Do you require the first move? (y/n): ")
    if go_first == "y":
        print("\nGo ahead take the first move.")
        human = X
        computer = O
    else:
        print("\nGood luck... I will go first.")
        computer = X
        human = O
    return computer,human


def new_board():
    """Create new game board."""
    board = []
    for square in range(NUM_SQUARES):
        board.append(EMPTY)
    return board


def display_board(board):
    """Display game board on screen."""
    print("\n\t", board[0], "|", board[1], "|", board[2])
    print("\t", "--------- ")
    print("\t", board[3], "|", board[4], "|", board[5])
    print("\t", "--------- ")
    print("\t", board[6], "|", board[7], "|", board[8], "\n")


def legal_moves(board):
    """Create list of legal moves."""
    moves = []
    for square in range(NUM_SQUARES):
        if board[square] == EMPTY:
            moves.append(square)
    return moves


def winner(board):
    """Determine the game winner."""
    WAYS_TO_WIN = ((0, 1, 2), (3, 4, 5),(6, 7, 8),(0, 3, 6),(1, 4, 7),(2, 5, 8),(0, 4, 8),(2, 4, 6))
    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner


# main
print("Here are the instructions to the Tic-Tac-Toe game:")
instructions()
print("Here they are again:")

answer_question("test")

input("\n\nPress the enter key to exit.")