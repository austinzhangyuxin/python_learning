import tkinter as tk
from tkinter import messagebox


def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


class PrimeCheckerApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Prime Number Checker")

        self.label = tk.Label(master, text="Enter a number:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=10)

        self.check_button = tk.Button(master, text="Check Prime", command=self.check_prime)
        self.check_button.pack(pady=10)

        self.result_label = tk.Label(master, text="")
        self.result_label.pack(pady=10)

    def check_prime(self):
        try:
            number = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid integer.")
            return

        if is_prime(number):
            self.result_label.config(text=f"{number} is a prime number.", fg="green")
        else:
            self.result_label.config(text=f"{number} is not a prime number.", fg="red")


def main():
    root = tk.Tk()
    app = PrimeCheckerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
