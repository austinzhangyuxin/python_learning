import tkinter as tk


class MultiplicationTableApp:
    def __init__(self, master, size=10):
        self.master = master
        self.master.title("Multiplication Table")
        self.size = size
        self.create_table()

    def create_table(self):
        for i in range(1, self.size + 1):
            for j in range(1, self.size + 1):
                result = i * j
                label = tk.Label(self.master, text=str(result), borderwidth=1, relief="solid", width=5, height=2)
                label.grid(row=i, column=j, padx=1, pady=1)


def main():
    root = tk.Tk()
    app = MultiplicationTableApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox
import random


class GridClickerGame:
    def __init__(self, master, rows=5, cols=5):
        self.master = master
        self.master.title("Grid Clicker Game")
        self.rows = rows
        self.cols = cols
        self.buttons = []
        self.max_number = -1

        self.create_grid()

    def create_grid(self):
        for i in range(self.rows):
            row_buttons = []
            for j in range(self.cols):
                number = random.randint(1, 100)
                button = tk.Button(self.master, text="?", width=10, height=3,
                                   command=lambda i=i, j=j, number=number: self.reveal_number(i, j, number))
                button.grid(row=i, column=j, padx=5, pady=5)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def reveal_number(self, i, j, number):
        button = self.buttons[i][j]
        button.config(text=str(number), state="disabled")

        if number > self.max_number:
            self.max_number = number
            self.highlight_max_number()

    def highlight_max_number(self):
        for row in self.buttons:
            for button in row:
                button.config(bg="SystemButtonFace")

        for i in range(self.rows):
            for j in range(self.cols):
                if self.buttons[i][j].cget("text") == str(self.max_number):
                    self.buttons[i][j].config(bg="yellow")


def main():
    root = tk.Tk()
    game = GridClickerGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
