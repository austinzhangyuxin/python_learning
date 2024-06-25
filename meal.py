meal = "An English muffin"
print("Breakfast: " + meal)

meal = "Sushi"
print("Lunch: " + meal)

meal = 'Curry Fish'
print("Dinner: " + meal)

# print('I can't do this') # this quotation doesn't close
print("I can't do this")

# print("He said "Hello world!"")
print('He said "Hello world!"')

import sys


def display_menu():
    print("\nWelcome to the Python Menu Example!")
    print("1. Option 1: Perform Action 1")
    print("2. Option 2: Perform Action 2")
    print("3. Option 3: Perform Action 3")
    print("4. Exit")


def option1():
    print("You selected Option 1.")
    # Replace with your logic for Option 1


def option2():
    print("You selected Option 2.")
    # Replace with your logic for Option 2


def option3():
    print("You selected Option 3.")
    # Replace with your logic for Option 3


def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()
