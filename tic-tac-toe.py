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
        winner = 0
        while winner == 0:
            self.print_board()
            self.take_turn(self.turn)
            self.change_turn()
            winner = self.check_winner()
        self.print_board()
        print(f'\nPlayer {winner} has won!' if winner != -
              1 else '\nDraw!')

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

    # Part 3

    def get_move(self):
        """Get input from user asking for their move as a tuple"""
        row = int(input('\nRow: '))
        col = int(input('Column: '))
        return (row, col)

    # Part 4
    def take_turn(self, player):
        """This is the driver method for a players turn"""

        print(f"It is Player {player}'s turn")

        valid = False
        move = None
        available_squares = self.get_available_squares()

        # AI
        if self.AI and player == self.AI_turn:
            move = self.smart_move()
        # Player
        else:
            while valid == False:
                move = self.get_move()
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
        self.board[move[0]][move[1]] = player

    # Part 5
    def check_winner(self):
        """
        Check if a player has won, there are 8 ways to win.
        Return the player who won 0 if nobody has won, and -1 if it is a draw
        """

        # Get lines
        rows = [row for row in self.board]
        cols = [[self.board[j][i] for j in range(
            len(self.board[0]))] for i in range(len(self.board))]
        diags = [[self.board[i][i] for i in range(len(self.board))], [
            self.board[i][len(self.board) - i - 1] for i in range(len(self.board))]]
        lines = rows + cols + diags

        # Check for winning line
        elems_set = set()
        for line in lines:
            line_elems = set(line)
            elems_set.update(line_elems)
            if len(line_elems) == 1:  # every elements of the line have the same value
                result = line_elems.pop()  # 0, 1, or 2
                if result != 0:
                    return result

        # No winning line
        return 0 if 0 in elems_set else -1

    # Part 6
    def random_move(self):
        """Returns a random move from the list of available squares."""
        available_moves = self.get_available_squares()
        move = random.choice(available_moves)
        return move

    # Part 7
    def winning_move(self, player):
        """Find a winning move for a player"""

        # Get moves
        moves = self.get_available_squares()

        for move in moves:
            # print('DEBUG move', move)

            # Simulate move
            # deep copy using list comprehension
            board_sim = [row[:] for row in self.board]
            board_sim[move[0]][move[1]] = player

            # print('DEBUG board_sim', board_sim)

            # Check for win
            row = board_sim[move[0]][:]
            col = [row[move[1]] for row in board_sim]
            # Diag(s)
            diags = []
            if move[0] == move[1]:
                diags.append([board_sim[i][i] for i in range(len(board_sim))])
            if move[0] == len(board_sim) - move[1] - 1:
                diags.append([board_sim[i][len(board_sim) - i - 1]
                             for i in range(len(board_sim))])

            # print('DEBUG row', row)
            # print('DEBUG col', col)
            # print('DEBUG diags', diags)
            # print('DEBUG len(diags)', len(diags))

            lines = []
            lines.append(row)
            lines.append(col)
            if len(diags) != 0:
                for diag in diags:
                    lines.append(diag)

            # print('DEBUG lines', lines)

            # Check for winning move
            for line in lines:
                line_elems = set(line)
                if len(line_elems) == 1:  # every elements of the line have the same value
                    result = line_elems.pop()  # 0, 1, or 2
                    if result != 0:
                        return move

        return None

    def threat_to_lose(self):
        # Run winning_move from other perspective
        return

    def smart_move(self):

        # If there is a winning move, win
        winning_move = self.winning_move(self.AI_turn)
        if winning_move:
            return winning_move

        # If there is a threat to lose, block
        blocking_move = self.threat_to_lose()
        if blocking_move:
            return blocking_move

        # Make random move
        return self.random_move()

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
    sim.AI = True
    sim.AI_turn = 2
    sim.play_game()

    # sim.board = [[2, 1, 1], [1, 2, 2], [2, 1, 1]]
    # print(sim.check_winner())

    # print(len(set([0, 0, 0])))
    # print(len(set([0, 1, 0])))
    # print(len(set([0, 1, 2])))
    # print(len(set([1, 1, 1])))
    # print(len(set([2, 2, 2])))
