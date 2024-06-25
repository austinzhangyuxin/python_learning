import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.guesses_left = 10

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text="Guess the number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(self.root)
        self.entry.pack(pady=5)

        self.submit_button = tk.Button(self.root, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=5)

    def check_guess(self):
        guess = int(self.entry.get())
        self.guesses_left -= 1

        if guess == self.secret_number:
            messagebox.showinfo("Congratulations!", f"You guessed the number {self.secret_number}!")
            self.reset_game()
        elif guess < self.secret_number:
            messagebox.showinfo("Incorrect", f"Too low! Guesses left: {self.guesses_left}")
        else:
            messagebox.showinfo("Incorrect", f"Too high! Guesses left: {self.guesses_left}")

        if self.guesses_left == 0:
            messagebox.showinfo("Game Over", f"Out of guesses! The number was {self.secret_number}.")
            self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.guesses_left = 10


def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
