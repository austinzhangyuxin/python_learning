# Replace ___ with your code

# get an integer input from the user
n = int(input("enter a number: "))

# using a loop, iterate from 1 to n (inclusive) and print n
for i in range(1, n + 1):
    print(i)

    # if the value of i is 3, break the loop
    if i == 3:
        break

# initial value of total will be 0
total = 0

n = float(input("Enter a number: "))

# loop until n is not equal to 0
while n != 0:
    # add the value of n to total
    total = total + n

    # take the input again
    n = float(input("Enter a number: "))

# print the total
print(f"Result: {total}")

# initial value of total will be 0
total = 0

# the condition of the loop is always True
# the only way to end this loop is by using break
while True:

    n = float(input("Enter a number: "))

    # if user enters 0, end the loop
    if n == 0:
        break

    # add the value of n to total
    total = total + n

# print the total
print(f"Result: {total}")

total = 0

while True:
    # get integer input
    n = int(input("enter a number"))

    if n <= 0:
        break

    total = total + n

# print the total
print(total)

for i in range(1, 101):

    if i == 3:
        break

    print(i)

import random


def example_break_loop():
    """Example of breaking out of a loop."""
    print("Example 1: Breaking out of a loop based on a condition")
    for i in range(10):
        print(i, end=' ')
        if i == 5:
            print("\nBreaking the loop at i = 5")
            break
    print("\nLoop finished.\n")


def game_break_loop():
    """Example of breaking out of a game loop."""
    print("Example 2: Breaking out of a game loop with user input")
    while True:
        user_input = input("Enter 'quit' to exit the game: ").strip().lower()
        if user_input == 'quit':
            print("Exiting the game loop.")
            break
        else:
            print("Unknown command. Try again.")
    print("\nGame loop finished.\n")


def nested_break_loop():
    """Example of breaking out of nested loops."""
    print("Example 3: Breaking out of nested loops")
    for i in range(1, 6):
        print(f"Outer loop iteration: {i}")
        for j in range(1, 11):
            print(j, end=' ')
            if j == 5:
                print("\nBreaking the inner loop at j = 5")
                break
        else:
            continue  # This is executed if the inner loop did NOT break
        print("\nInner loop finished.")
        break
    print("\nOuter loop finished.\n")


def main():
    example_break_loop()
    game_break_loop()
    nested_break_loop()


if __name__ == "__main__":
    main()
