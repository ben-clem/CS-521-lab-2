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
    def __init__(self, AI: bool = False, AI_turn: int = 2) -> 'TicTacToeSim':
        # Initialize the simulation
        # Set up board as a 2D list, turn to player 1, and ai to false
        # Required fields: board, turn, AI, AI_turn

        # !!! Just watched the video example and not supposed to use parameters but input instead => implement that in part 8, use default value for the moment

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

    def change_turn(self):
        # Change turn to other player
        return

    def play_game(self):
        # This is the driver method for the simulation
        return

    # Part 2
    def print_board(self):
        # Print the state of the board using X (player 1) and O (player 2)
        return

    # Part 3
    def get_move(self):
        # Get input from user asking for their move as a tuple
        return None

    # Part 4
    def take_turn(self, player):
        # This is the driver method for a players turn
        return

    def get_available_squares(self):
        # Get a list of available squares as tuples (row,col)
        return None

    def make_move(self, move, player):
        return

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
        return

    # Part 8
    def get_settings(self):
        # At the start of the simulation, get settings from the user
        # Decide whether to play vs AI and if so whether the user is first or second

        #### ONLY FOR TESTING #####
        #### DO NOT PUT TESTING CODE OUTSIDE OF HERE ####
if __name__ == '__main__':
    sim = TicTacToeSim()
    sim.play_game()
