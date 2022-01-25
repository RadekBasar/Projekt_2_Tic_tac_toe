import random

BOARD_SIZE = 3
BOARD_SIZE_SQUARE = BOARD_SIZE ** 2

NO_ITEM = ' '
PLAYER_O_ITEM = 'O'
PLAYER_X_ITEM = 'X'
DRAW = '-'
CONTINUE_GAME = 'C'

INVALID_INDEX = -1


def start():
    print_rules()
    board = [NO_ITEM, NO_ITEM, NO_ITEM, NO_ITEM, NO_ITEM, NO_ITEM, NO_ITEM, NO_ITEM, NO_ITEM]  # [' ', ' ', ...]
    print_board(board)
    end_game = False
    player_o_move = True
    while not end_game:
        print("============================================")
        if player_o_move: # == True
            if not user_move(board):
                continue
        else:
            computer_move(board)
        print("============================================")
        print_board(board)
        status = check_game(board)
        end_game = is_end_game(status)
        player_o_move = not player_o_move  # player_o_move = not True -> player_o_move = False


def print_rules():
    print('''Welcome to Tic Tac Toe
========================================
GAME RULES:
Each player can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
========================================
Let's start the game''')


def print_board(board): # ['O', 'O', 'O', ' ', 'X', ...]
    for row in range(BOARD_SIZE):
        for column in range(BOARD_SIZE):
            print("|", end='')
            index = row * BOARD_SIZE + column
            board_item = board[index]
            print(" " + board_item + " ", end='')
        print("|")
    print("+" + 3 * "---+")


def user_move(board):
    user_input = input("Player o | Please enter your move number: ") # 3
    index = get_board_index(user_input, board) # 2
    if index == INVALID_INDEX: # 2 == -1 -> False
        return False
    board[index] = PLAYER_O_ITEM
    return True


def get_board_index(user_input, board):
    if not user_input.isdigit() or not ((int(user_input) - 1) in range(BOARD_SIZE_SQUARE)):
        print("Invalid input, please enter number between 1 and " + str(BOARD_SIZE_SQUARE))
        return INVALID_INDEX # -1
    index = int(user_input) - 1 # 2
    if board[index] != NO_ITEM:
        print("Field is not empty")
        return INVALID_INDEX # -1
    return index # 2


def computer_move(board):
    found = False
    while not found:
        random_index = random.randint(0, BOARD_SIZE_SQUARE - 1) # 3
        if board[random_index] == NO_ITEM:
            board[random_index] = PLAYER_X_ITEM
            print("Player x | Please enter your move number: " + str(random_index + 1))
            found = True


def check_game(board):
    if (board[0] == board[1] == board[2] != NO_ITEM):  # 'O' == 'O' == 'O' != ' '
        return board[0] # 'O'
    elif (board[3] == board[4] == board[5] != NO_ITEM):
        return board[3]
    elif (board[6] == board[7] == board[8] != NO_ITEM):
        return board[6]
    elif (board[0] == board[3] == board[6] != NO_ITEM):
        return board[0]
    elif (board[1] == board[4] == board[7] != NO_ITEM):
        return board[1]
    elif (board[2] == board[5] == board[8] != NO_ITEM):
        return board[2]
    elif (board[0] == board[4] == board[8] != NO_ITEM):
        return board[0]
    elif (board[2] == board[4] == board[6] != NO_ITEM):
        return board[2]
    elif NO_ITEM not in board:
        return DRAW # '-'
    else:
        return CONTINUE_GAME # 'C'


def is_end_game(status):
    if status == PLAYER_O_ITEM:
        print("============================================")
        print("Player O wins!")
        return True
    elif status == PLAYER_X_ITEM:
        print("============================================")
        print("Player X wins!")
        return True
    elif status == DRAW:
        print("============================================")
        print("Draw")
        return True
    else:
        return False


start()
