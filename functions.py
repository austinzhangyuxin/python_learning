def happy_birthday(name, age):
    print(f"happy_birthday to {name} at {age} years old!")


def multiply(x, y):
    result = x * y
    print(f'The result of {x} multiply by {y} is {result}.')
    # return x * y


multiply(4, 5)

multiply(10, 40)

multiply(100, 80)


def exponential(base, power):
    result = base ** power
    print(f'The result of {base} to the power of {power} is {result}.')
    # return x * y


exponential(4, 2)

exponential(10, 100)


# define print_numbers() function
def print_numbers():
    print(5)
    print(100)


# call print_number() twice
print_numbers()
print_numbers()


# define a function to add numbers
def add_numbers(n1, n2):
    result = n1 + n2
    print("The sum is", result)


# Replace ___ with your code

# create the get_product() function
def get_product(number1, number2):
    result = number1 * number2
    return result


# get integer inputs from the user
n1 = int(input(""))
n2 = int(input(""))

# call the function with n1 and n2 as arguments
# and print the return value

total = get_product(n1, n2)
print(total)

number1 = 5
number2 = 6
add_numbers(number1, number2)


# Replace ___ with your code

# define the function add_three_numbers()
def add_three_numbers(n1, n2, n3):
    result = n1 + n2 + n3
    print(result)


# take input for num1, num2, num3
num1 = int(input(""))
num2 = int(input(""))
num3 = int(input(""))

# call the function with num1, num2 and num3
add_three_numbers(num1, num2, num3)


def add_numbers(n1, n2):
    result = n1 + n2
    return result


total = add_numbers(10, 20)
print(total)  # 30

print(add_numbers(20, 30))  # 50


# Replace ___ with your code

# define the is_positive_or_negative() function
def is_positive_or_negative(number):
    if number >= 0:
        return True
    else:
        return False


# take integer input from the user
input_number = int(input("num: "))

# call the function
print(is_positive_or_negative(input_number))

import random

# Define global variables for game state
rooms = ["Hall", "Kitchen", "Living Room", "Bedroom", "Bathroom"]
current_room = random.choice(rooms)
inventory = []
score = 0


def display_intro():
    print("Welcome to the Adventure Game!")
    print("Explore different rooms, solve puzzles, and collect items.")
    print("Your goal is to find the treasure and earn points!\n")


def display_options():
    print("\nOptions:")
    print("1. Move to another room")
    print("2. Search current room")
    print("3. Check inventory")
    print("4. Quit game")


def move_to_room():
    global current_room
    current_room = random.choice(rooms)
    print(f"You moved to the {current_room}.")


def search_room():
    global score
    print(f"You are searching the {current_room}...")
    found_item = random.choice(["Key", "Map", "Potion", "Coin", None])
    if found_item:
        print(f"You found a {found_item}!")
        inventory.append(found_item)
        score += 10
    else:
        print("You didn't find anything.")


def check_inventory():
    print("Inventory:")
    if inventory:
        for item in inventory:
            print("-", item)
    else:
        print("Your inventory is empty.")


def main_game_loop():
    global score
    while True:
        print(f"\nCurrent Room: {current_room} | Score: {score}")
        display_options()
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            move_to_room()
        elif choice == '2':
            search_room()
        elif choice == '3':
            check_inventory()
        elif choice == '4':
            print("Exiting game...")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


def main():
    display_intro()
    main_game_loop()


if __name__ == "__main__":
    main()


# -------------------------------------

def compute_sum(number):
    total = 0

    # iterate loop from 1 to number
    for i in range(1, number + 1):
        total = total + i

    return total


total = compute_sum(10)
print(total)  # Output: 55

total = compute_sum(100)
print(total)  # Output: 5050
