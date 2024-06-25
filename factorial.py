def factorial_iterative(n):
    """Computes the factorial of a non-negative integer n iteratively."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Example usage
try:
    number = int(input("Enter a non-negative integer: "))
    print(f"{factorial_iterative(number)}")
except ValueError as e:
    print(e)


# --------------------------------------------
def factorial_iterative(n):
    """Computes the factorial of a non-negative integer n iteratively."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


# Example usage
try:
    number = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {number} is {factorial_iterative(number)}.")
except ValueError as e:
    print(e)


# -------------------------------------

def factorial_recursive(n):
    """Computes the factorial of a number recursively."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)


def main():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            raise ValueError("The input must be a non-negative integer.")
        print(f"The factorial of {num} is {factorial_recursive(num)}.")
    except ValueError as e:
        print(f"Invalid input: {e}")


if __name__ == "__main__":
    main()


# -----------------------------

def factorial_recursive(n):
    """Computes the factorial of a non-negative integer n recursively."""
    if not isinstance(n, int) or n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


# Example usage
try:
    number = int(input("Enter a non-negative integer: "))
    print(f"The factorial of {number} is {factorial_recursive(number)}.")
except ValueError as e:
    print(e)


import logging

# Configure logging
logging.basicConfig(filename='app.log', filemode='w', level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(message)s')


class Calculator:
    def __init__(self):
        pass

    def add(self, a: float, b: float) -> float:
        """Returns the sum of two numbers."""
        return a + b

    def factorial(self, n: int) -> int:
        """Returns the factorial of a non-negative integer."""
        if n < 0:
            logging.error("Factorial is not defined for negative numbers.")
            return "Factorial is not defined for negative numbers."
        elif n == 0 or n == 1:
            return 1
        else:
            result = 1
            for i in range(2, n + 1):
                result *= i
            return result


class Greeter:
    def greet(self, name: str) -> str:
        """Greets the person whose name is passed as an argument."""
        return f"Hello, {name}!"


def main():
    calculator = Calculator()
    greeter = Greeter()

    while True:
        print("\nMenu:")
        print("1. Greet")
        print("2. Add two numbers")
        print("3. Calculate factorial")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter your name: ")
            print(greeter.greet(name))
            logging.info(f"Greeted user: {name}")

        elif choice == '2':
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = calculator.add(num1, num2)
                print(f"The sum of {num1} and {num2} is {result}.")
                logging.info(f"Added {num1} and {num2} to get {result}")
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                logging.error("Invalid input for addition.")

        elif choice == '3':
            try:
                num = int(input("Enter a non-negative integer: "))
                result = calculator.factorial(num)
                print(f"The factorial of {num} is {result}.")
                logging.info(f"Calculated factorial of {num} to get {result}")
            except ValueError:
                print("Invalid input. Please enter a valid non-negative integer.")
                logging.error("Invalid input for factorial.")

        elif choice == '4':
            print("Exiting the program.")
            logging.info("Program exited by the user.")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 4.")
            logging.warning("User entered an invalid menu choice.")


if __name__ == "__main__":
    main()
