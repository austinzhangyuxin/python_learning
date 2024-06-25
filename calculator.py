def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y


def calculator():
    print("Welcome to Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")

            another_calculation = input("Do you want to perform another calculation? (yes/no): ")
            if another_calculation.lower() != 'yes':
                break
        else:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    calculator()

import math


class AdvancedCalculator:
    def __init__(self):
        self.memory = 0

    def add(self, x, y):
        """Adds two numbers."""
        return x + y

    def subtract(self, x, y):
        """Subtracts y from x."""
        return x - y

    def multiply(self, x, y):
        """Multiplies two numbers."""
        return x * y

    def divide(self, x, y):
        """Divides x by y."""
        if y == 0:
            raise ValueError("Error: Division by zero.")
        return x / y

    def power(self, x, y):
        """Raises x to the power of y."""
        return x ** y

    def square_root(self, x):
        """Returns the square root of x."""
        if x < 0:
            raise ValueError("Error: Cannot calculate square root of a negative number.")
        return math.sqrt(x)

    def factorial(self, x):
        """Returns the factorial of x."""
        if x < 0:
            raise ValueError("Error: Factorial is not defined for negative numbers.")
        return math.factorial(x)

    def memory_store(self, value):
        """Stores a value in memory."""
        self.memory = value

    def memory_recall(self):
        """Recalls the value stored in memory."""
        return self.memory

    def memory_clear(self):
        """Clears the memory."""
        self.memory = 0

    def calculate_expression(self, expression):
        """Evaluates a mathematical expression."""
        try:
            result = eval(expression, {'__builtins__': None}, vars(math))
            return result
        except Exception as e:
            return f"Error: {str(e)}"

    def run_calculator(self):
        """Runs the advanced calculator."""
        print("Welcome to the Advanced Calculator!")
        print("Available operations: +, -, *, /, ** (power), sqrt (square root), ! (factorial)")
        print("Memory functions: MS (Store), MR (Recall), MC (Clear)")
        print("Enter 'exit' to quit.\n")

        while True:
            user_input = input("Enter an expression or operation: ").strip().lower()

            if user_input == 'exit':
                print("Exiting the calculator. Goodbye!")
                break

            elif user_input.startswith('ms'):
                try:
                    value = float(user_input.split()[1])
                    self.memory_store(value)
                    print(f"Stored {value} in memory.")
                except ValueError:
                    print("Invalid input. Please enter a number after 'MS'.")

            elif user_input == 'mr':
                print(f"Memory recall: {self.memory_recall()}")

            elif user_input == 'mc':
                self.memory_clear()
                print("Memory cleared.")

            else:
                result = self.calculate_expression(user_input)
                print(f"Result: {result}\n")


if __name__ == "__main__":
    calculator = AdvancedCalculator()
    calculator.run_calculator()

import math


class AdvancedCalculator:
    def __init__(self):
        self.variables = {}

    def evaluate_expression(self, expression):
        try:
            result = eval(expression, {"__builtins__": None}, self.safe_math())
            return result
        except ZeroDivisionError:
            return "Error: Division by zero."
        except Exception as e:
            return f"Error: {e}"

    def safe_math(self):
        safe_dict = {}
        safe_dict.update(math.__dict__)
        safe_dict.update(self.variables)
        return safe_dict

    def assign_variable(self, name, value):
        self.variables[name] = value

    def parse_input(self, user_input):
        if "=" in user_input:
            var_name, expression = user_input.split("=", 1)
            var_name = var_name.strip()
            expression = expression.strip()
            result = self.evaluate_expression(expression)
            if isinstance(result, (int, float)):
                self.assign_variable(var_name, result)
                return f"{var_name} = {result}"
            else:
                return result
        else:
            return self.evaluate_expression(user_input)

    def run(self):
        print("Advanced Calculator")
        print("Type 'exit' to quit.")
        print("You can use basic arithmetic operations, trigonometric functions, and more.")
        print("Assign variables using the format: x = 5 + 3")
        print("Use variables in expressions: x * 2")

        while True:
            user_input = input(">> ")
            if user_input.lower() == 'exit':
                break
            result = self.parse_input(user_input)
            print(result)


if __name__ == "__main__":
    calc = AdvancedCalculator()
    calc.run()

# ---------------------------------------
import tkinter as tk
from tkinter import messagebox


class AdvancedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")

        self.entry = tk.Entry(root, width=30, font=('Arial', 18), borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=5, padx=10, pady=10)

        # Create buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('+', 1, 3), ('C', 1, 4),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3), ('AC', 2, 4),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('*', 3, 3), ('%', 3, 4),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('/', 4, 3), ('^', 4, 4),
            ('sin', 5, 0), ('cos', 5, 1), ('tan', 5, 2), ('(', 5, 3), (')', 5, 4)
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), command=lambda t=text: self.click(t))
            button.grid(row=row, column=column, padx=10, pady=10)

    def click(self, text):
        if text == 'C':
            current = self.entry.get()[:-1]
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current)
        elif text == 'AC':
            self.entry.delete(0, tk.END)
        elif text == '=':
            try:
                expression = self.entry.get()
                result = eval(expression)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)
            except Exception as e:
                messagebox.showerror("Error", f"Invalid input: {e}")
        else:
            current = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current + text)


def main():
    root = tk.Tk()
    app = AdvancedCalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
