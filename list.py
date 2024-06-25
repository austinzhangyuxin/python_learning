# Create a list named list1 containing 5 elements
list1 = [1, 2, 3, 4, 5]

# Use the len() function to find the length of list1
length_of_list1 = len(list1)

# Print the length of list1
print(f"{length_of_list1}")
# ------------------------------------
import random
import time


class MemoryChallengeGame:
    def __init__(self, num_elements=5):
        self.num_elements = num_elements
        self.elements = self.generate_elements()
        self.time_to_memorize = 10  # Time in seconds to memorize the list

    def generate_elements(self):
        items = ["apple", "banana", "orange", "grape", "cherry", "mango", "peach", "pear", "plum", "berry"]
        return random.sample(items, self.num_elements)

    def display_list(self):
        print("Memorize this list of items:")
        for item in self.elements:
            print(item)
        print(f"\nYou have {self.time_to_memorize} seconds to memorize the list.")

    def clear_console(self):
        # Clear the console (works for Windows, Mac, Linux)
        print("\n" * 100)

    def play_game(self):
        self.display_list()
        time.sleep(self.time_to_memorize)
        self.clear_console()

        print("Now, try to recall the items in the list.")
        recalled_items = []
        for i in range(self.num_elements):
            item = input(f"Enter item {i + 1}: ").strip().lower()
            recalled_items.append(item)

        correct_items = [item for item in recalled_items if item in self.elements]
        score = len(correct_items)
        print(f"\nYou recalled {score} out of {self.num_elements} items correctly.")
        print(f"The original list was: {self.elements}")
        print(f"Your recalled items were: {recalled_items}")

        if score == self.num_elements:
            print("Congratulations! You have a perfect memory!")
        else:
            print("Good try! Keep practicing to improve your memory.")


if __name__ == "__main__":
    game = MemoryChallengeGame(num_elements=5)
    game.play_game()

# -------------------------------
# Replace ___ with your code

# create a list containing items 9, 11 and 15
# assign the list to the odd_numbers variable
odd_numbers = [3, 9, 11]

# print the second item
print(odd_numbers[2])


# Function to display the menu
def display_menu():
    print("\nMenu:")
    print("1. Append an animal to the list")
    print("2. Insert an animal at a specific position")
    print("3. Remove an animal from the list")
    print("4. Display the current list")
    print("5. Display a slice of the list")
    print("6. Exit")


# Function to handle appending an animal
def append_animal(animals):
    animal = input("Enter the name of the animal to append: ")
    animals.append(animal)
    print(f"{animal} has been added to the list.")


# Function to handle inserting an animal
def insert_animal(animals):
    animal = input("Enter the name of the animal to insert: ")
    position = int(input(f"Enter the position to insert {animal} at (0 to {len(animals)}): "))
    if 0 <= position <= len(animals):
        animals.insert(position, animal)
        print(f"{animal} has been inserted at position {position}.")
    else:
        print("Invalid position!")


# Function to handle removing an animal
def remove_animal(animals):
    animal = input("Enter the name of the animal to remove: ")
    if animal in animals:
        animals.remove(animal)
        print(f"{animal} has been removed from the list.")
    else:
        print(f"{animal} is not in the list!")


# Function to display a slice of the list
def display_slice(animals):
    start = int(input("Enter the start index for the slice: "))
    end = int(input("Enter the end index for the slice: "))
    if 0 <= start < len(animals) and 0 <= end <= len(animals):
        print(f"The slice from index {start} to {end} is: {animals[start:end]}")
    else:
        print("Invalid indices!")


# Main function to run the program
def main():
    animals = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            append_animal(animals)
        elif choice == '2':
            insert_animal(animals)
        elif choice == '3':
            remove_animal(animals)
        elif choice == '4':
            print(f"The current list of animals is: {animals}")
        elif choice == '5':
            display_slice(animals)
        elif choice == '6':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")


if __name__ == "__main__":
    main()
# -------------------------
# Replace ___ with your code

# create an empty list
animals = ["dog"]

# append "dog" to the list

print(animals)

# append "cat" to the list
animals.append("cat")

print(animals)


# ----------------------------
def custom_length(lst):
    count = 0
    for _ in lst:
        count += 1
    return count


# Example list
my_list = [10, 20, 30, 40]

# Find the length of the list without using len()
length_of_list = custom_length(my_list)

# Print the result
print(f"{length_of_list}")