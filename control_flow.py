numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
threshold = 7

for number in numbers:
    if number % 2 != 0:
        continue

    while True:
        if number > threshold:
            break
        else:
            print(number)
            break

import random

# Define global variables for game state
rooms = {
    "Hall": {
        "description": "You are in a grand hall with many doors leading to different rooms.",
        "items": ["Key", "Map"],
        "exits": {"Kitchen", "Living Room"}
    },
    "Kitchen": {
        "description": "You are in a messy kitchen with pots and pans scattered around.",
        "items": ["Knife", "Potion"],
        "exits": {"Hall", "Garden"}
    },
    "Living Room": {
        "description": "You are in a cozy living room with a fireplace and comfortable chairs.",
        "items": ["Book", "Coin"],
        "exits": {"Hall", "Bedroom"}
    },
    "Bedroom": {
        "description": "You are in a bedroom with a large bed and a nightstand.",
        "items": ["Lamp", "Clothes"],
        "exits": {"Living Room", "Bathroom"}
    },
    "Bathroom": {
        "description": "You are in a clean bathroom with a shower and a mirror.",
        "items": ["Towel", "Soap"],
        "exits": {"Bedroom"}
    },
    "Garden": {
        "description": "You are in a lush garden with colorful flowers and a small pond.",
        "items": ["Shovel", "Seed"],
        "exits": {"Kitchen"}
    }
}

current_room = "Hall"
inventory = []
score = 0


def display_intro():
    print("Welcome to the Advanced Adventure Game!")
    print("Explore different rooms, solve puzzles, and collect items.")
    print("Your goal is to find the treasure and earn points!\n")


def display_room():
    room_info = rooms[current_room]
    print(f"\n{current_room}")
    print(room_info['description'])
    print("Items in the room:", room_info['items'])
    print("Exits:", ', '.join(room_info['exits']))


def move_to_room(destination):
    global current_room
    if destination in rooms[current_room]['exits']:
        current_room = destination
        print(f"You moved to the {current_room}.")
    else:
        print("You can't go that way.")


def search_room():
    global score
    room_info = rooms[current_room]
    print(f"You are searching the {current_room}...")
    found_item = random.choice(room_info['items'])
    if found_item:
        print(f"You found a {found_item}!")
        inventory.append(found_item)
        room_info['items'].remove(found_item)
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
        display_room()
        print(f"\nCurrent Room: {current_room} | Score: {score}")
        display_options()
        choice = input("Enter your choice: ").strip().lower()

        if choice == 'move':
            destination = input("Enter room to move to: ").strip().title()
            move_to_room(destination)
        elif choice == 'search':
            search_room()
        elif choice == 'inventory':
            check_inventory()
        elif choice == 'quit':
            print("Exiting game...")
            break
        else:
            print("Invalid choice. Please enter 'move', 'search', 'inventory', or 'quit'.")


def display_options():
    print("\nOptions:")
    print("1. Move to another room")
    print("2. Search current room")
    print("3. Check inventory")
    print("4. Quit game")


def main():
    display_intro()
    main_game_loop()


if __name__ == "__main__":
    main()
