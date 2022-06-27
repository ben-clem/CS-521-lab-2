"""
Name: Benoît Clemenceau
GitHub username: ben-clem (https://github.com/ben-clem)
Collaborators: None
Extension: No
Sources:
"""

import random


class TicTacToeSim:

    # Part 1
    def __init__(self) -> 'TicTacToeSim':
        """
        Initialize the simulation
        Set up board as a 2D list, turn to player 1, and ai to false
        """
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        self.turn = 1
        self.AI = False
        self.AI_turn = None

    def change_turn(self):
        """Change turn to other player"""
        try:
            if self.turn == 1:
                self.turn = 2
            elif self.turn == 2:
                self.turn = 1
            else:
                raise ValueError('turn variable must be either 1 or 2')
        except Exception as err:
            print(err)

    def play_game(self):
        """This is the driver method for the simulation"""
        print('\nPlayer 1 is X, Player 2 is O')
        while True:
            self.print_board()
            self.take_turn(self.turn)
            self.change_turn()

    # Part 2
    def print_board(self):
        """Print the state of the board using X (player 1) and O (player 2)"""

        chars = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 1:
                    chars[i][j] = 'X'
                elif self.board[i][j] == 2:
                    chars[i][j] = 'O'

        print('\n  Col 0   1   2  ')
        print('Row ╔═══╦═══╦═══╗')
        print(f' 0  ║ {chars[0][0]} ║ {chars[0][1]} ║ {chars[0][2]} ║')
        print('    ╠═══╬═══╬═══╣')
        print(f' 1  ║ {chars[1][0]} ║ {chars[1][1]} ║ {chars[1][2]} ║')
        print('    ╠═══╬═══╬═══╣')
        print(f' 2  ║ {chars[2][0]} ║ {chars[2][1]} ║ {chars[2][2]} ║')
        print('    ╚═══╩═══╩═══╝')

        print(f"It is Player {self.turn}'s turn")

    # Part 3
    def get_move(self):
        """Get input from user asking for their move as a tuple"""
        row = int(input('\nRow: '))
        col = int(input('Column: '))
        return (row, col)

    # Part 4
    def take_turn(self, player):
        """This is the driver method for a players turn"""

        valid = False
        available_squares = self.get_available_squares()

        while valid == False:
            move = self.get_move()
            # print('DEBUG move', move)
            # print('DEBUG available_squares', available_squares)
            if move in available_squares:
                valid = True
            else:
                print('Invalid move!')

        self.make_move(move, player)

    def get_available_squares(self):
        """Get a list of available squares as tuples (row,col)"""
        squares = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.board[i][j] == 0:
                    squares.append((i, j))
        return squares

    def make_move(self, move, player):
        # print('DEBUG self.board', self.board)
        # print('DEBUG move', move)
        # print('DEBUG player', player)
        self.board[move[0]][move[1]] = player

    # Part 5
    def check_winner(self):
        # Check if a player has won, there are 8 ways to win.
        # Return the player who won 0 if nobody has won, and -1 if it is a draw
        return 0

    # Part 6
    def random_move(self):
        """Returns a random move from the list of available squares."""
        available_moves = self.get_available_squares()
        move = random.choice(available_moves)
        return move

    # Part 7
    def winning_move(self, player):
        # Find a winning move for a player
        return None

    def threat_to_lose(self):
        # Run winning_move from other perspective
        return

    def smart_move(self):
        # If there is a winning move, win
        # If there is a threat to lose, block
        # Make random move

        random.choice(available_moves)

        return

    # Part 8
    def get_settings(self):
        # At the start of the simulation, get settings from the user
        # Decide whether to play vs AI and if so whether the user is first or second

        # , AI: bool = False, AI_turn: int = 2

        try:
            if not isinstance(AI, bool):
                raise TypeError('AI parameter must be of bool type')
            else:
                self.AI = AI

            if not isinstance(AI_turn, int):
                raise TypeError('AI_turn parameter must be of int type')
            elif not AI_turn == 1 or 2:
                raise ValueError('AI_turn parameter must be either 1 or 2')
            else:
                self.AI_turn = AI_turn

            self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

            if not AI or AI and AI_turn == 2:
                self.turn = 1
            else:
                self.turn = 2

        except Exception as err:
            print(err)

        #### ONLY FOR TESTING #####
        #### DO NOT PUT TESTING CODE OUTSIDE OF HERE ####
if __name__ == '__main__':
    sim = TicTacToeSim()
    sim.play_game()
