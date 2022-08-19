# user interface

from tabulate import tabulate

import ai
import utils as utils
import argparse
import time

counter = 0
board = utils.board


def print_board():
    print(tabulate(board, tablefmt='fancy_grid', stralign="center"))


def get_move():
    move = int(input("Which square do you want to pick: "))
    x = int(move / utils.width)
    y = (move % utils.width)
    return x, y


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("-p1", "--player1", required=False, help="Who is player 1")
    ap.add_argument("-p2", "--player2", required=False, help="Who is player 2")
    args = vars(ap.parse_args())
    utils.find_playerTypes(args["player1"], args["player2"])
    print("LETS PLAY")

    winner = False
    x, y = None, None
    print_board()
    while not winner and not utils.is_tie():
        time.sleep(utils.delay)
        if utils.get_counter() % 2 == 0:
            turn = utils.player1
        elif utils.get_counter() % 2 == 1:
            turn = utils.player2
        x, y = utils.pick_move(board, turn)
        utils.make_move(turn, board, (x, y))
        winner = utils.check_winner()
        print_board()
    if utils.get_winner() == utils.get_playerLetter(utils.player1):
        print("Player 1 (" + utils.get_playerType(utils.player1) + ") wins!!!")
    elif utils.get_winner() == utils.get_playerLetter(utils.player2):
        print("Player 2 (" + utils.get_playerType(utils.player2) + ") wins!!!")
    else:
        print("This is a tie")


utils.generate()
main()
