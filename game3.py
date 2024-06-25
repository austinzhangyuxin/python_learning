import tkinter as tk
from tkinter import messagebox


class ConnectFour:
    def __init__(self, root):
        self.root = root
        self.root.title("Connect Four")

        # Game variables
        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'
        self.moves_left = self.rows * self.cols

        # Create GUI elements
        self.create_board()
        self.create_buttons()

    def create_board(self):
        self.buttons = [[None] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                btn = tk.Button(self.root, text=" ", width=7, height=3, font=('Arial', 20), command=lambda c=col: self.drop_piece(c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def create_buttons(self):
        self.reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=self.rows + 1, columnspan=self.cols)

    def drop_piece(self, col):
        for row in range(self.rows-1, -1, -1):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.current_player
                self.buttons[row][col].config(text=self.current_player, state=tk.DISABLED, disabledforeground='black')

                if self.check_winner(row, col):
                    self.game_over()
                    return

                if self.moves_left == 1:
                    self.game_over()
                    return

                self.current_player = 'O' if self.current_player == 'X' else 'X'
                self.moves_left -= 1
                return

    def check_winner(self, row, col):
        directions = [(-1, 0), (0, -1), (-1, -1), (-1, 1)]  # vertical, horizontal, diagonal up-left, diagonal up-right

        for d_row, d_col in directions:
            count = 1
            # Check in both directions
            for direction in (-1, 1):
                r, c = row + direction * d_row, col + direction * d_col
                while 0 <= r < self.rows and 0 <= c < self.cols and self.board[r][c] == self.current_player:
                    count += 1
                    r += direction * d_row
                    c += direction * d_col

            if count >= 4:
                return True

        return False

    def game_over(self):
        messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
        self.disable_board()

    def reset_game(self):
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.current_player = 'X'
        self.moves_left = self.rows * self.cols

        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[row][col].config(text=" ", state=tk.NORMAL)

    def disable_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                self.buttons[row][col].config(state=tk.DISABLED)


def main():
    root = tk.Tk()
    game = ConnectFour(root)
    root.mainloop()


if __name__ == "__main__":
    main()
