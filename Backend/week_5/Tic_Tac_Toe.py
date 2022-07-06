# Create a class TicTacToe that will enable you to write a complete program to play the
# game of tic-tac-toe. The class contains a 3-by-3 double-subscripted list of letters. The constructor
# should initialize the empty board to all zeros. Allow two human players. Wherever the first player
# moves, place an "X" in the specified square; place an "O" wherever the second player moves. Each
# move must be to an empty square. After each move, determine whether the game has been won and
# whether the game is a draw. [Note: If you feel ambitious, modify your program so that the computer
# makes the moves for one of the players automatically. Also, allow the player to choose whether to go
# first or second.]

from re import X


class Tic_Tac_Toe:
    def __init__(self) -> None:
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
                    ]

        self.move =[]

    def player_symbol():
        symbol_1 = X
        symbol_2 = 0

    
    def isFull(board, symbol_1, symbol_2):
        pass