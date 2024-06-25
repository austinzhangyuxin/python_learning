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
