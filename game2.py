import tkinter as tk
from tkinter import messagebox


class TicTacToeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Advanced Tic-Tac-Toe")
        self.board = [" "] * 9
        self.buttons = []
        self.current_player = "X"
        self.create_board()

    def create_board(self):
        for i in range(3):
            for j in range(3):
                btn = tk.Button(self.master, text=" ", font=('Arial', 20), width=6, height=3,
                                command=lambda row=i, col=j: self.player_move(row, col))
                btn.grid(row=i, column=j)
                self.buttons.append(btn)

    def player_move(self, row, col):
        index = 3 * row + col
        if self.board[index] == " ":
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_win(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
            elif " " not in self.board:
                messagebox.showinfo("Game Over", "It's a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
                self.computer_move()

    def computer_move(self):
        best_score = -float('inf')
        best_move = None
        for i in range(9):
            if self.board[i] == " ":
                self.board[i] = "O"
                score = self.minimax(False)
                self.board[i] = " "
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = "O"
        self.buttons[best_move].config(text="O")
        if self.check_win("O"):
            messagebox.showinfo("Game Over", "Computer wins!")
            self.reset_game()
        elif " " not in self.board:
            messagebox.showinfo("Game Over", "It's a tie!")
            self.reset_game()
        else:
            self.current_player = "X"

    def minimax(self, is_maximizing):
        if self.check_win("O"):
            return 1
        elif self.check_win("X"):
            return -1
        elif " " not in self.board:
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "O"
                    score = self.minimax(False)
                    self.board[i] = " "
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if self.board[i] == " ":
                    self.board[i] = "X"
                    score = self.minimax(True)
                    self.board[i] = " "
                    best_score = min(score, best_score)
            return best_score

    def check_win(self, player):
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6]
        ]
        for condition in win_conditions:
            if all(self.board[i] == player for i in condition):
                return True
        return False

    def reset_game(self):
        for i in range(9):
            self.board[i] = " "
            self.buttons[i].config(text=" ")
        self.current_player = "X"


def main():
    root = tk.Tk()
    game = TicTacToeGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()
