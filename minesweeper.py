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
