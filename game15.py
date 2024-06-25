import tkinter as tk
from tkinter import messagebox
import random


class MemoryGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Memory Game")

        self.numbers = list(range(1, 9)) * 2  # Numbers 1 to 8 repeated twice for pairs
        random.shuffle(self.numbers)  # Shuffle the numbers

        self.buttons = []
        self.selected = []  # List to hold currently selected buttons
        self.matches = set()  # Set to hold matched numbers

        self.create_widgets()

    def create_widgets(self):
        for i in range(4):
            for j in range(4):
                button = tk.Button(self.master, text=" ", width=4, height=2,
                                   command=lambda row=i, col=j: self.on_button_click(row, col))
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append(button)

    def on_button_click(self, row, col):
        index = row * 4 + col
        button = self.buttons[index]

        # Check if button is already matched or selected
        if index in self.matches or button.cget("text") != " ":
            return

        number = self.numbers[index]
        button.config(text=str(number))

        self.selected.append((index, number))

        if len(self.selected) == 2:
            self.master.after(500, self.check_matches)

    def check_matches(self):
        if len(self.selected) == 2:
            index1, number1 = self.selected[0]
            index2, number2 = self.selected[1]

            if number1 == number2:
                self.matches.add(index1)
                self.matches.add(index2)
                messagebox.showinfo("Match!", "You found a pair!")
            else:
                self.buttons[index1].config(text=" ")
                self.buttons[index2].config(text=" ")

            self.selected = []

        if len(self.matches) == 16:
            messagebox.showinfo("Congratulations!", "You found all pairs!")
            self.master.destroy()


def main():
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
