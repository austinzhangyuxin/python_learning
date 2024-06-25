def display_board(board):
    """Display Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):
    """Check if the player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


def is_board_full(board):
    """Check if the board is full."""
    for row in board:
        if any(cell == '_' for cell in row):
            return False
    return True


def tic_tac_toe():
    """Run Tic-Tac-Toe game."""
    board = [['_', '_', '_'],
             ['_', '_', '_'],
             ['_', '_', '_']]
    player = 'X'

    while True:
        display_board(board)
        row = int(input(f"Player {player}, enter row (1-3): ")) - 1
        col = int(input(f"Player {player}, enter column (1-3): ")) - 1

        if board[row][col] == '_':
            board[row][col] = player
            if check_winner(board, player):
                display_board(board)
                print(f"Player {player} wins!")
                break
            elif is_board_full(board):
                display_board(board)
                print("It's a tie!")
                break
            else:
                player = 'O' if player == 'X' else 'X'
        else:
            print("That cell is already taken! Try again.")


if __name__ == "__main__":
    tic_tac_toe()


# ---------------------------------

class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # Initialize empty board
        self.current_player = 'X'
        self.winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
            (0, 4, 8), (2, 4, 6)  # Diagonals
        ]

    def print_board(self):
        """Prints the current state of the board."""
        for row in [self.board[i * 3:(i + 1) * 3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')
        print('-' * 13)

    def available_moves(self):
        """Returns a list of indices of available moves."""
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def make_move(self, move):
        """Places current player's mark on the board at the given move."""
        self.board[move] = self.current_player

    def check_for_winner(self):
        """Checks if the current player has won."""
        for combo in self.winning_combinations:
            if all(self.board[i] == self.current_player for i in combo):
                return True
        return False

    def is_board_full(self):
        """Checks if the board is full (tie situation)."""
        return all(spot != ' ' for spot in self.board)

    def switch_player(self):
        """Switches the current player."""
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def play_game(self):
        """Main function to play the Tic-Tac-Toe game."""
        print("Welcome to Advanced Tic-Tac-Toe!")
        print("The board is numbered from 0-8, corresponding to the positions as shown below.")
        self.print_board()

        while True:
            move = None
            if self.current_player == 'X':
                while move not in self.available_moves():
                    try:
                        move = int(input("Enter your move (0-8): "))
                    except ValueError:
                        print("Invalid input. Please enter a number between 0 and 8.")
            else:
                move = self.get_computer_move()

            self.make_move(move)
            self.print_board()

            if self.check_for_winner():
                print(f"Player {self.current_player} wins!")
                break
            elif self.is_board_full():
                print("It's a tie!")
                break

            self.switch_player()

    def get_computer_move(self):
        """Generates a random computer move."""
        return random.choice(self.available_moves())


if __name__ == "__main__":
    import random

    game = TicTacToe()
    game.play_game()
