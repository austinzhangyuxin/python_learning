def main():
    # Get input from the user
    number = int(input("Enter an integer: "))

    # Initialize count variable
    count = 0

    # Handle negative numbers by taking the absolute value
    number = abs(number)

    # Loop to count digits
    while number != 0:
        number = number // 10  # Remove the last digit
        count += 1             # Increase the count

    # Special case for zero
    if count == 0:
        count = 1

    # Print the result
    print(f"{count}")


if __name__ == "__main__":
    main()


import tkinter as tk
from tkinter import messagebox


def count_digits(number):
    number = abs(number)  # Handle negative numbers
    count = 0

    # Loop to count digits
    while number != 0:
        number = number // 10  # Remove the last digit
        count += 1             # Increase the count

    # Special case for zero
    if count == 0:
        count = 1

    return count

def display_result():
    try:
        number = int(entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid integer.")
        return

    digit_count = count_digits(number)
    result_label.config(text=f"The number of digits is: {digit_count}")


# Set up the GUI
root = tk.Tk()
root.title("Digit Counter")

frame = tk.Frame(root, padx=10, pady=10)
frame.pack()

instruction_label = tk.Label(frame, text="Enter an integer:")
instruction_label.pack(pady=5)

entry = tk.Entry(frame)
entry.pack(pady=5)

submit_button = tk.Button(frame, text="Count Digits", command=display_result)
submit_button.pack(pady=5)

result_label = tk.Label(frame, text="")
result_label.pack(pady=5)

root.mainloop()
