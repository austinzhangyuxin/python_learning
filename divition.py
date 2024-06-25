# Replace ___ with your code

input_number = int(input("input_number: "))

# write your code here
if input_number % 5 == 0:
    print("The number is divisible by 5")
else:
    print("The number is not divisible by 5")

import sys


def divide_numbers(dividend, divisor):
    try:
        quotient = dividend / divisor
        return quotient
    except ZeroDivisionError:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")


def get_number(prompt, type_func):
    while True:
        try:
            user_input = input(prompt)
            number = type_func(user_input)
            return number
        except ValueError:
            print("Error: Please enter a valid number.")


def main():
    print("Welcome to the Advanced Division Calculator!")

    while True:
        print("\nMenu:")
        print("1. Divide")
        print("2. Exit")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == '1':
            try:
                dividend = get_number("Enter the dividend: ", float)
                divisor = get_number("Enter the divisor: ", float)
                result = divide_numbers(dividend, divisor)
                print(f"\nResult: {dividend} / {divisor} = {result:.2f}")
            except ZeroDivisionError as zd_error:
                print(zd_error)
            except KeyboardInterrupt:
                print("\nKeyboard interrupt detected. Exiting...")
                sys.exit(1)
        elif choice == '2':
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()
