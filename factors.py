def main():
    # Get input from the user
    number = int(input("Enter an integer: "))

    # Print all factors of the number

    for i in range(1, number + 1):
        if number % i == 0:
            print(i)


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox


def get_factors(number):
    factors = set()
    for i in range(1, int(number ** 0.5) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number // i)
    return sorted(factors)


def display_factors():
    try:
        number = int(entry.get())
        if number <= 0:
            raise ValueError("The number must be a positive integer.")
    except ValueError as e:
        messagebox.showerror("Invalid input", f"Error: {e}")
        return

    factors = get_factors(number)
    result_label.config(text=f"Factors of {number} are:\n" + ', '.join(map(str, factors)))


# Set up the GUI
root = tk.Tk()
root.title("Factors Finder")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

instruction_label = tk.Label(frame, text="Enter a positive integer:")
instruction_label.pack(pady=5)

entry = tk.Entry(frame)
entry.pack(pady=5)

submit_button = tk.Button(frame, text="Find Factors", command=display_factors)
submit_button.pack(pady=5)

result_label = tk.Label(frame, text="")
result_label.pack(pady=5)

root.mainloop()
