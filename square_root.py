import math

number = 625

square_root = number ** (1 / 2)
print(f"Square root of {number} is {square_root}")

print(f'Square root of {number} using math module math.sqrt() is {math.sqrt(number)}')

import math


def calculate_square_root(number):
    try:
        if number >= 0:
            result = math.sqrt(number)
            return result
        else:
            result = complex(0, math.sqrt(abs(number)))
            return result
    except ValueError:
        return "Error: Cannot compute square root of negative number using real numbers."


def main():
    print("Welcome to the Advanced Square Root Calculator!")

    try:
        number = float(input("Enter a number to find its square root: "))

        square_root = calculate_square_root(number)

        if isinstance(square_root, complex):
            print(f"The square root of {number} is: {square_root.real} + {square_root.imag}i")
        else:
            print(f"The square root of {number} is: {square_root}")

    except ValueError:
        print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
