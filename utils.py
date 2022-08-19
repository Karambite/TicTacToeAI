# rules
import string

import utils as utils
import ai as ai
import numpy as np

board = np.zeros([3, 3], dtype='object')
counter = 0
legal_moves = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
rows = []
cols = []
diagonals = [[(0, 0), (1, 1), (2, 2)], [(0, 2), (1, 1), (2, 0)]]
player1 = {"letter": "X", "type": None}
player2 = {"letter": "O", "type": None}
winner = None
width = 3
size = 9
delay = 0


def set_playerType(player, type):
    player["type"] = type


def get_playerType(player):
    return player["type"]


def get_playerLetter(player):
    return player["letter"]


def get_counter() -> int:
    return counter


def get_legalMoves(board):
    all_legal_moves = []
    count = 0
    for i in range(utils.width):
        for j in range(utils.width):
            if board[i, j] == count:
                all_legal_moves.append((i, j))
            count += 1
    return all_legal_moves


def winning_rows():
    for i in range(utils.width):
        row = []
        for j in range(utils.width):
            row.append((i, j))
        rows.append(row)


def winning_cols():
    for i in range(utils.width):
        col = []
        for j in range(utils.width):
            col.append((j, i))
        cols.append(col)


def new_board():
    count = 0
    for i, j in legal_moves:
        board[i, j] = count
        count += 1


def make_move(player, board, move):
    global counter
    global legal_moves
    legal_moves = get_legalMoves(board)
    utils.update(move)
    board[move] = player["letter"]
    counter += 1
    return board


def unmove(player, board, move):
    global counter
    global legal_moves
    legal_moves = get_legalMoves(board)
    legal_moves.append(move)
    board[move] = (move[0] * 3) + move[1]
    counter -= 1
    return board


def update(move):
    legal_moves.remove(move)


def opponent(player):
    if player == player1:
        return player2
    return player1


def get_winner():
    return winner


def check_winner():
    global winner
    for line in rows:
        element = board[line[0]]
        if element is None:
            continue
        else:
            if board[line[1]] == element and board[line[2]] == element:
                winner = element
                return True

    for line in cols:
        element = board[line[0]]
        if element is None:
            continue
        else:
            if board[line[1]] == element and board[line[2]] == element:
                winner = element
                return True

    for line in diagonals:
        element = board[line[0]]
        if element is None:
            continue
        else:
            if board[line[1]] == element and board[line[2]] == element:
                winner = element
                return True

    return False


def is_tie():
    if len(legal_moves) == 0:
        return True
    return False


def generate():
    winning_rows()
    winning_cols()
    new_board()


def find_playerTypes(type1, type2):
    global delay
    if type1 == 'h':
        set_playerType(player1, "Human")
    elif type1 == 'r':
        set_playerType(player1, "Random AI")
    elif type1 == 'w':
        set_playerType(player1, "Winning AI")
    elif type1 == 'l':
        set_playerType(player1, "Winning and Losing AI")
    elif type1 == 'm':
        set_playerType(player1, "Minimax AI")

    if type2 == 'h':
        set_playerType(player2, "Human")
    elif type2 == 'r':
        set_playerType(player2, "Random AI")
    elif type2 == 'w':
        set_playerType(player2, "Winning AI")
    elif type2 == 'l':
        set_playerType(player2, "Winning and Losing AI")
    elif type2 == 'm':
        set_playerType(player2, "Minimax AI")

    if player1["type"] != "Human" and player2["type"] != "Human":
        delay = 2


def pick_move(board, player):
    if player["type"] == "Human":
        x, y = ai.human()
    elif player["type"] == "Random AI":
        x, y = ai.random_ai(board)
    elif player["type"] == "Winning AI":
        x, y = ai.find_winning_move_ai(board, player)
    elif player["type"] == "Winning and Losing AI":
        x, y = ai.find_winning_move_and_losing_ai(board, player)
    elif player["type"] == "Minimax AI":
        x, y = ai.minimax_ai(board, player)
    return x, y

"""legal_moves1 = utils.get_legalMoves(_board)
            for moves1 in legal_moves1:
                print(moves)
                fboard = _board.copy()
                fboard = utils.make_move(utils.opponent(player), fboard, moves1)
                print(fboard)"""
