import random


# here we will create the board for the AI
def environment(board):
    # the board is a list of 10 strings that represents i
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# this allows the user to select from X or O for the board game as inputs
def player_input():
    letter = ' '
    while not (letter == 'X' or letter == 'O'):
        print('Please select from X or O')
        letter = input().upper() & input().lower()

    # the first element in the list will be the player's letter and the second will be the AI
    if letter == 'X' or 'x':
        return ['X', 'O']
    else:
        return ['O', 'X']


# random choose player that goes first
def first():
    if random.randint(0, 1) == 0:
        return 'TTT Bot'
    else:
        return 'User'


# this function returns true if the player desires to play again
def repeat():
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# this function does the movement on the board for the game-play
def move(board, letter, motion):
    board[motion] = letter


# Given a board and player's letter
# this returns True if player has won
def winner(board, letter):
    # across the top
    return ((board[7] == letter and board[8] == letter and board[9] == letter) or
            # across the middle
            (board[4] == letter and board[5] == letter and board[6] == letter) or
            # across the bottom
            (board[1] == letter and board[2] == letter and board[3] == letter) or
            # down the left side
            (board[7] == letter and board[4] == letter and board[1] == letter) or
            # down the middle
            (board[8] == letter and board[5] == letter and board[2] == letter) or
            # down the right side
            (board[9] == letter and board[6] == letter and board[3] == letter) or
            # diagonal
            (board[7] == letter and board[5] == letter and board[3] == letter) or
            (board[9] == letter and board[5] == letter and board[1] == letter))


# this will be a duplicate of the board
def environment_copy(board):
    duplicate = []
    for i in board:
        duplicate.append(i)
    return duplicate


# this will return true if the move that's been passed is free on the board
def free_space(board, move):
    return board[move] == ' '


# allow the player to make move
def player_move(board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        print('Make your next move by selecting a number! (1-9)')
        move = input()
    return int(move)


