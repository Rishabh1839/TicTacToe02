from random import choice

combo_indices = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

EMPTY_SIGN = '.'
AI_SIGN = 'X' or 'x'
OPPONENT_SIGN = 'O' or 'o'

#here we will provide user options for the user to interact with the game
print("Welcome to TIC TAC TOE by Rishabh Singh")
print("Here we have created a Tic Tac Toe game in Python for users to play")
print("The user's goal is to get 3 in a row for any signs they user from either X or O")

# here we will be defining our board
def print_board(board):
    print(" ")
    print(' '.join(board[:3]))
    print('=' * 5)
    print(' '.join(board[3:6]))
    print('=' * 5)
    print(' '.join(board[6:]))
    print(" ")

# defining the opponent move while it generates new board every time it's the users turn
def opponent_move(board, row, column):
    index = 3 * (row - 1) + (column - 1)
    if board[index] == EMPTY_SIGN:
        return board[:index] + OPPONENT_SIGN + board[index+1:]
    return board

# defining all moves that include ai and opponent moves
def all_moves(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            new_board = board[:i] + sign + board[i + 1:]
            move_list.append(new_board)
            if win(new_board) == AI_SIGN:
                return[new_board]
    return move_list

#defining all moves from the list
def all_moves_from_list(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            move_list.append(board[:i] + sign + board[i + 1:])
            return move_list

# defining an ai   move
def ai_move(board):
    boards = all_moves(board, AI_SIGN)
    for new_board in boards:
        if win(new_board) == AI_SIGN:
            print("YOU WON! CONGRATS")
            return new_board
        return choice(boards)
    return choice(all_moves(board, AI_SIGN))

# defining who won
def win(board):
    for index in combo_indices:
        if board[index[0]] == board[index[1]] == board[index[2]] != EMPTY_SIGN:
            return board[index[0]]
        return EMPTY_SIGN

# defining the game loop
def game_loop():
    board = EMPTY_SIGN * 9
    empty_cell_count = 9
    game_ends = False
    while empty_cell_count > 0 and not game_ends:
        if empty_cell_count % 2 == 1:
            board = ai_move(board)
        else:
            row = int(input('Enter the row please: '))
            column = int(input('Enter the Column: '))
            board = opponent_move(board, row, column)
        print_board(board)
        game_ends = win(board) != EMPTY_SIGN
        empty_cell_count = sum(1 for cell in board if cell == EMPTY_SIGN)
        print("The game has been ended, would you like to replay?")

game_loop()
