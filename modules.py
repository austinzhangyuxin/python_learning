import math

def main():
    # Get two integer inputs from the user
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))

    # Calculate the greatest common divisor (GCD) using the math.gcd() function
    gcd_result = math.gcd(num1, num2)

    # Print the result
    print(f"{gcd_result}")


# Call the main function
if __name__ == "__main__":
    main()

# game_logic.py
import random


class NumberGuessingGame:
    def __init__(self):
        self.secret_number = random.randint(1, 100)

    def reset_game(self):
        self.secret_number = random.randint(1, 100)

    def check_guess(self, guess):
        if guess < self.secret_number:
            return "Too low! Try again."
        elif guess > self.secret_number:
            return "Too high! Try again."
        else:
            return "Congratulations! You guessed it!"


# Example of usage in a script
if __name__ == "__main__":
    game = NumberGuessingGame()
    print(game.secret_number)  # For testing purposes
