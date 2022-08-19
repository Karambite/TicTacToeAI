# TicTacToeAI
A terminal Tic Tac Toe game that uses different playing style algorithms. Trying to upload this on a microcontroller with micropython and create a hands-on toy.

How to play?
- It's Normal TicTacToe
- read the documentation for argparse to get a better understanding of how to choose which interfaces should play aginst each other
- argparse has two arguments player 1 (-p1) and player 2 (-p2)
- These arguments can accept different interfaces
  * human (h)
  * random (r)
  * winning AI (w)
  * winning and losing AI (l)
  * minimax AI (m)

Example
- human vs winning AI -> python tictactoeAI.py -p1 h -p2 w
