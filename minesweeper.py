import random


class Minesweeper:
    def __init__(self, size, num_mines):
        self.size = size
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.mine_positions = self.place_mines()
        self.visited = [[False for _ in range(size)] for _ in range(size)]
        self.game_over = False

    def place_mines(self):
        positions = set()
        while len(positions) < self.num_mines:
            pos = (random.randint(0, self.size - 1), random.randint(0, self.size - 1))
            positions.add(pos)
        for (x, y) in positions:
            self.board[x][y] = 'M'
        return positions

    def print_board(self, reveal=False):
        for x in range(self.size):
            row = ""
            for y in range(self.size):
                if self.visited[x][y] or reveal:
                    row += self.board[x][y] + " "
                else:
                    row += ". "
            print(row)
        print()

    def get_adjacent_mines(self, x, y):
        count = 0
        for i in range(max(0, x - 1), min(self.size, x + 2)):
            for j in range(max(0, y - 1), min(self.size, y + 2)):
                if (i, j) in self.mine_positions:
                    count += 1
        return count

    def reveal(self, x, y):
        if self.board[x][y] == 'M':
            self.game_over = True
            print("Game Over! You hit a mine!")
            self.print_board(reveal=True)
            return

        if self.visited[x][y]:
            return

        self.visited[x][y] = True
        adjacent_mines = self.get_adjacent_mines(x, y)
        if adjacent_mines == 0:
            self.board[x][y] = '0'
            for i in range(max(0, x - 1), min(self.size, x + 2)):
                for j in range(max(0, y - 1), min(self.size, y + 2)):
                    if not self.visited[i][j]:
                        self.reveal(i, j)
        else:
            self.board[x][y] = str(adjacent_mines)

    def check_win(self):
        for x in range(self.size):
            for y in range(self.size):
                if self.board[x][y] != 'M' and not self.visited[x][y]:
                    return False
        return True

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                x, y = map(int, input("Enter coordinates to reveal (row col): ").split())
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    print("Invalid coordinates. Try again.")
                    continue
                self.reveal(x, y)
                if self.check_win():
                    print("Congratulations! You've cleared the minefield!")
                    self.print_board(reveal=True)
                    break
            except ValueError:
                print("Invalid input. Enter row and column numbers separated by a space.")


# Example usage
if __name__ == "__main__":
    size = 5
    num_mines = 5
    game = Minesweeper(size, num_mines)
    game.play()


import tkinter as tk
import random

class Minesweeper:
    def __init__(self, root, rows, cols, num_mines):
        self.root = root
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines

        self.board = [[0] * cols for _ in range(rows)]
        self.mines = set()
        self.revealed = [[False] * cols for _ in range(rows)]

        self.create_widgets()

        self.generate_mines()
        self.calculate_numbers()

    def create_widgets(self):
        self.buttons = [[None] * self.cols for _ in range(self.rows)]

        for row in range(self.rows):
            for col in range(self.cols):
                btn = tk.Button(self.root, text="", width=3, height=1, font=('Arial', 10),
                                command=lambda r=row, c=col: self.click(r, c))
                btn.grid(row=row, column=col)
                self.buttons[row][col] = btn

    def generate_mines(self):
        while len(self.mines) < self.num_mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.mines.add((row, col))
            self.board[row][col] = -1  # -1 represents a mine

    def calculate_numbers(self):
        directions = [(-1, -1), (-1, 0), (-1, 1),
                      (0, -1),          (0, 1),
                      (1, -1), (1, 0), (1, 1)]

        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == -1:
                    continue  # skip if it's a mine

                count = 0
                for d_row, d_col in directions:
                    new_row, new_col = row + d_row, col + d_col
                    if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                        if self.board[new_row][new_col] == -1:
                            count += 1
                self.board[row][col] = count

    def click(self, row, col):
        if (row, col) in self.mines:
            self.buttons[row][col].config(text="*", state=tk.DISABLED)
            self.reveal_board()
            tk.messagebox.showinfo("Game Over", "You clicked on a mine! Game over.")
        else:
            self.reveal(row, col)
            if self.check_win():
                tk.messagebox.showinfo("Congratulations", "You win!")

    def reveal(self, row, col):
        if self.revealed[row][col]:
            return

        self.revealed[row][col] = True
        self.buttons[row][col].config(text=self.board[row][col], state=tk.DISABLED)

        if self.board[row][col] == 0:
            directions = [(-1, -1), (-1, 0), (-1, 1),
                          (0, -1),          (0, 1),
                          (1, -1), (1, 0), (1, 1)]
            for d_row, d_col in directions:
                new_row, new_col = row + d_row, col + d_col
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    self.reveal(new_row, new_col)

    def reveal_board(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) in self.mines:
                    self.buttons[row][col].config(text="*", state=tk.DISABLED)
                else:
                    self.buttons[row][col].config(text=self.board[row][col], state=tk.DISABLED)

    def check_win(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.mines and not self.revealed[row][col]:
                    return False
        return True


def main():
    root = tk.Tk()
    root.title("Minesweeper")

    # Define the size of the board and number of mines
    rows = 8
    cols = 8
    num_mines = 10

    minesweeper = Minesweeper(root, rows, cols, num_mines)

    root.mainloop()


if __name__ == "__main__":
    main()
