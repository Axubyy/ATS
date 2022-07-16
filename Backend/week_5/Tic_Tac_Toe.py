# Create a class TicTacToe that will enable you to write a complete program to play the
# game of tic-tac-toe. The class contains a 3-by-3 double-subscripted list of letters. The constructor
# should initialize the empty board to all zeros. Allow two human players. Wherever the first player
# moves, place an "X" in the specified square; place an "O" wherever the second player moves. Each
# move must be to an empty square. After each move, determine whether the game has been won and
# whether the game is a draw. [Note: If you feel ambitious, modify your program so that the computer
# makes the moves for one of the players automatically. Also, allow the player to choose whether to go
# first or second.]
import random


class Tic_Tac_Toe:
    count = 0
    def __init__(self) -> None:
        self.board = [
            [0,0,0],
            [0,0,0],
            [0,0,0]
                    ]

    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
            
    def get_random_first_player(self):
        return random.randint(0, 1)

    def fix_position(self, row, col, player):
        self.board[row][col] = player

    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == 0:
                    return False
        return True

    def change_player_turns(self, player):
        return 'X' if player == 'O' else 'O'

    def is_current_player_winner(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if not self.board[i][j] == player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        # for row in self.board:
        #     for item in row:
        #         if item == '0':
        #             return False
        # return True

    def start(self):
        # self.create_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")

            self.show_board()

            row, col = list(map(int, input("Enter row and column numbers to fix spot (two numbers with space(s) in between): ").split()))
            print()
            self.fix_position(row - 1, col - 1, player)

            # checking whether player is won or not
            if self.is_current_player_winner(player):
                print(f"Player {player} is the game winner!")
                print("Thanks for Playing, Bye! Exiting ...")
                break

            # checking whether the game is draw or not
            if self.is_board_filled():
                print("Game Draw! Exiting ....")
                break

            # swapping the turn
            player = self.change_player_turns(player)

        # showing the final view of board
        print()
        self.show_board()

    
 



board = Tic_Tac_Toe()

print(board.show_board())
# print(board.get_random_first_player())
# print(board.fix_position())
print(board.start())
print(board.is_current_player_winner())