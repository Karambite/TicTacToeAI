# still under testing
import random as random

import utils as utils
import test


def random_ai(board):
    # print(random.choice(utils.legal_moves))
    print(utils.get_legalMoves(board))
    x, y = random.choice(utils.get_legalMoves(board))
    print("My turn, I choose: (" + str(x) + "," + str(y) + ")")
    return x, y


def find_winning_move_and_losing_ai(board, player):
    x_1, y_1 = find_winning_move(board, player)
    x_2, y_2 = find_winning_move(board, utils.opponent(player))
    if (x_1, y_1) != (-1, -1):
        return x_1, y_1
    elif (x_2, y_2) != (-1, -1):
        return x_2, y_2
    return random_ai(board)


def find_winning_move_ai(board, player):
    x, y = find_winning_move(board, player)
    if (x, y) == (-1, -1):
        return random_ai(board)
    return x, y


def find_winning_move(board, player):
    # check horizontal
    for line in utils.rows:
        player_count = 0
        empty_count = 0
        for x, y in line:
            if board[x, y] == utils.get_playerLetter(player):
                player_count += 1
            elif type(board[x, y]) is int:
                empty_x, empty_y = x, y
                empty_count += 1
        if player_count == 2 and empty_count == 1:
            return empty_x, empty_y
        # print(player_count, empty_count)

    # check vertical
    for line in utils.cols:
        player_count = 0
        empty_count = 0
        for x, y in line:
            if board[x, y] == utils.get_playerLetter(player):
                player_count += 1
            elif type(board[x, y]) is int:
                empty_x, empty_y = x, y
                empty_count += 1
        if player_count == 2 and empty_count == 1:
            return empty_x, empty_y
    # check diagonal
    for line in utils.diagonals:
        player_count = 0
        empty_count = 0
        for x, y in line:
            if board[x, y] == utils.get_playerLetter(player):
                player_count += 1
            elif type(board[x, y]) is int:
                empty_x, empty_y = x, y
                empty_count += 1
        if player_count == 2 and empty_count == 1:
            return empty_x, empty_y

    return -1, -1


def human():
    valid = True
    while valid:
        move = int(input("Which square do you want to pick: "))
        x = int(move / utils.width)
        y = (move % utils.width)
        if (x, y) in utils.legal_moves:
            valid = False
        else:
            print("Illegal Move, pick again")
    return x, y


def minimax_ai(board, player):
    print(test.minimax_algo(board, player))
    return 1, 1










