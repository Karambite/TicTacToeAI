import utils as utils
import tictactoe as ttt


def minimax_algo(board, player):
    bestScore = float('-inf')
    best_Move = (None, None)
    for move in utils.legal_moves:
        score = find_bestScore(board, player, True)
        if score >= bestScore:
            bestScore = score
            best_Move = move
    return move


def find_bestScore(board, player, is_maximizing):

    winner_player = utils.get_winner()
    tie = utils.is_tie()

    if player == winner_player:
        return 1
    elif player == utils.opponent(winner_player):
        return -1
    elif tie:
        return 0
    else:
        scores = []
        print(board)
        for moves in utils.get_legalMoves(board):
            _board = board
            print(moves)
            print(_board)
            print(board)
            print(player)
            print(utils.opponent(player))
            if not utils.get_counter() == 9:
                utils.make_move(player, _board, moves)
                if is_maximizing:
                    print("HI!")
                    scores.append(find_bestScore(_board, player, False))
                else:
                    scores.append(find_bestScore(_board, utils.opponent(player), True))
                utils.unmove(player, _board, moves)

        print("HI:")
        print(scores)
        if is_maximizing:
            return max(scores)
        else:
            return min(scores)


    y = 1
    x = 0
    return 1, (x, y)
