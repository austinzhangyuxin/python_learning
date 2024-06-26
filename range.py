# Create a sequence of numbers using the range() function
sequence = range(4, 11, 3)

# Convert the sequence to a tuple using the tuple() function
sequence_tuple = tuple(sequence)

# Print the tuple
print(sequence_tuple)


import tkinter as tk
from tkinter import messagebox
import random


class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Number Guessing Game")

        # Generate a random number between 1 and 100
        self.secret_number = random.randint(1, 100)

        # Setup the GUI elements
        self.label = tk.Label(master, text="Guess a number between 1 and 100")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit Guess", command=self.check_guess)
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return

        if guess < 1 or guess > 100:
            messagebox.showerror("Out of range", "Please guess a number between 1 and 100.")
            return

        if guess < self.secret_number:
            self.result_label.config(text="Too low! Try again.")
        elif guess > self.secret_number:
            self.result_label.config(text="Too high! Try again.")
        else:
            self.result_label.config(text="Congratulations! You guessed it!")
            self.reset_game()

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.entry.delete(0, tk.END)
        messagebox.showinfo("Game Reset", "A new number has been generated. Start guessing again!")


def main():
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
