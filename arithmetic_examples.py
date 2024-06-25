import math

an_int = 2
a_float = 3.5
# print("an_int + 3")
print(an_int + 3)

print(a_float + an_int)
print(10 / 6)
# print(10/0)


# the following code gives ZeroDivisionError: division by zero
# is_this_zero = 1244-1244
# print(10/is_this_zero)

length = 12
width = 8

print(length * width)

length = 8
print(length * width)
print()
print()

print('Exponents mathematics')
print(5 * 5 * 5 * 5 * 5 * 5 * 5)
print(5 ** 7)
print()
print(7 ** 5)
print(7 * 7 * 7 * 7 * 7)

print()
print(4 ** 0.5)
print(49 ** 0.5)
print(1 % 2)
print(2 % 2)
print(3 % 2)
print(4 % 2)

print(math.pi)

print(10 / 3)

import random
import time


def generate_question():
    """Generates a random arithmetic question."""
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operator = random.choice(['+', '-', '*', '/'])

    # Ensure division results in an integer
    if operator == '/' and num1 % num2 != 0:
        num1 = num2 * random.randint(1, 10)  # Change num1 to make division work

    question = f"What is {num1} {operator} {num2}? "
    return question, eval(f'{num1}{operator}{num2}')


def math_game():
    """Runs the math game."""
    print("Welcome to the Advanced Math Game!")
    print("You will be asked to solve arithmetic problems.")
    print("Type 'exit' at any time to end the game.\n")

    score = 0
    while True:
        question, answer = generate_question()
        user_input = input(question).strip().lower()

        if user_input == 'exit':
            print(f"\nGame over! Your final score is: {score}")
            break

        try:
            user_answer = float(user_input)
            if user_answer == answer:
                print("Correct!")
                score += 1
            else:
                print(f"Incorrect. The correct answer was: {answer}")
        except ValueError:
            print("Invalid input. Please enter a number or 'exit'.")

        time.sleep(1)  # Pause for 1 second before next question


if __name__ == "__main__":
    math_game()
