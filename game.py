import random


class DungeonGame:
    def __init__(self):
        self.player_health = 100
        self.player_score = 0
        self.dungeon_map = [
            "Start", "Room with treasure", "Empty room", "Room with enemy", "Boss room"
        ]
        self.current_room = 0

    def play(self):
        print("Welcome to the Dungeon Game!")
        print("You are starting your adventure in the dungeon.\n")

        while self.current_room < len(self.dungeon_map):
            print(f"Current room: {self.dungeon_map[self.current_room]}")
            print(f"Player health: {self.player_health}")
            print(f"Player score: {self.player_score}\n")

            action = input("Choose your action (move forward / retreat): ").lower().strip()

            if action == "move forward":
                self.explore_room()
                self.current_room += 1
            elif action == "retreat":
                print("You retreat from the dungeon. Game over!")
                break
            else:
                print("Invalid action! Please choose 'move forward' or 'retreat'.\n")

        if self.current_room == len(self.dungeon_map):
            print("Congratulations! You have reached the end of the dungeon.")
            print(f"Final score: {self.player_score}")

    def explore_room(self):
        room_type = self.dungeon_map[self.current_room]

        if room_type == "Empty room":
            print("You found an empty room. Nothing here.")

        elif room_type == "Room with treasure":
            treasure = random.randint(1, 20)
            print(f"You found a room with treasure worth {treasure} points!")
            self.player_score += treasure

        elif room_type == "Room with enemy":
            enemy_health = random.randint(10, 30)
            print(f"Uh oh! You encounter an enemy with {enemy_health} health.")
            while enemy_health > 0 and self.player_health > 0:
                player_attack = random.randint(5, 15)
                enemy_health -= player_attack
                print(f"You attack the enemy for {player_attack} damage.")
                if enemy_health > 0:
                    enemy_attack = random.randint(3, 10)
                    self.player_health -= enemy_attack
                    print(f"The enemy attacks you for {enemy_attack} damage.")
                    print(f"Your health: {self.player_health}\n")
            if self.player_health <= 0:
                print("You have been defeated by the enemy. Game over!")
                self.current_room = len(self.dungeon_map)
            else:
                print("You defeated the enemy and continue your journey!\n")
                self.player_score += 10  # Reward for defeating enemy

        elif room_type == "Boss room":
            boss_health = 50
            print("You have reached the boss room!")
            while boss_health > 0 and self.player_health > 0:
                player_attack = random.randint(10, 20)
                boss_health -= player_attack
                print(f"You attack the boss for {player_attack} damage.")
                if boss_health > 0:
                    boss_attack = random.randint(5, 15)
                    self.player_health -= boss_attack
                    print(f"The boss attacks you for {boss_attack} damage.")
                    print(f"Your health: {self.player_health}\n")
            if self.player_health <= 0:
                print("You have been defeated by the boss. Game over!")
                self.current_room = len(self.dungeon_map)
            else:
                print("Congratulations! You defeated the boss and completed the dungeon!\n")
                self.player_score += 50  # Reward for defeating boss


# Main function to start the game
def main():
    game = DungeonGame()
    game.play()


if __name__ == "__main__":
    main()
# ----------------------------
import random


class TextAdventureGame:
    def __init__(self):
        self.player_name = ""
        self.player_health = 100
        self.player_experience = 0
        self.player_inventory = []
        self.current_location = "Town"
        self.quest_completed = False

    def play(self):
        self.intro()

        while not self.quest_completed:
            self.print_location_info()
            self.handle_player_action()

        self.game_over()

    def intro(self):
        print("Welcome to the Text Adventure Game!")
        self.player_name = input("Enter your name: ")
        print(f"Hello, {self.player_name}! Let's begin your adventure.\n")

    def print_location_info(self):
        print(f"You are in {self.current_location}.")
        print(f"Health: {self.player_health}")
        print(f"Experience Points: {self.player_experience}")
        print(f"Inventory: {', '.join(self.player_inventory)}")
        print()

    def handle_player_action(self):
        action = input("Choose your action (explore / talk / fight / inventory / quit): ").lower().strip()

        if action == "explore":
            self.explore()
        elif action == "talk":
            self.talk()
        elif action == "fight":
            self.fight()
        elif action == "inventory":
            self.show_inventory()
        elif action == "quit":
            self.quest_completed = True
        else:
            print("Invalid action! Please choose one of the available actions.\n")

    def explore(self):
        exploration_outcome = random.choice(["Nothing found.", "You found an item!", "You encountered an enemy!"])

        print(f"You explore {self.current_location}. {exploration_outcome}\n")

        if "item" in exploration_outcome.lower():
            item_found = random.choice(["Potion", "Sword", "Shield"])
            print(f"You found a {item_found}!")
            self.player_inventory.append(item_found)
        elif "enemy" in exploration_outcome.lower():
            self.fight()

    def talk(self):
        npc_name = random.choice(["Guard", "Merchant", "Wizard"])
        print(f"You talk to {npc_name} in {self.current_location}.")
        if npc_name == "Guard":
            print("Guard: Be careful in your travels, adventurer.")
        elif npc_name == "Merchant":
            print("Merchant: Take a look at my wares!")
            self.player_inventory.append("Gold Coin")
        elif npc_name == "Wizard":
            print("Wizard: Seek out the ancient artifacts to unlock great powers!")
            self.player_experience += 20

    def fight(self):
        enemy_health = random.randint(20, 50)
        print(f"You encounter an enemy with {enemy_health} health!")

        while enemy_health > 0 and self.player_health > 0:
            player_attack = random.randint(10, 30)
            enemy_health -= player_attack
            print(f"You attack the enemy for {player_attack} damage.")

            if enemy_health > 0:
                enemy_attack = random.randint(5, 20)
                self.player_health -= enemy_attack
                print(f"The enemy attacks you for {enemy_attack} damage.")
                print(f"Your health: {self.player_health}\n")

        if self.player_health <= 0:
            print("You have been defeated by the enemy. Game over!")
            self.quest_completed = True
        else:
            print("You defeated the enemy and continue your journey!\n")
            self.player_experience += 30

    def show_inventory(self):
        print("Inventory:")
        if self.player_inventory:
            for item in self.player_inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")

    def game_over(self):
        print(f"Congratulations, {self.player_name}! You completed the quest and finished your adventure.")


# Main function to start the game
def main():
    game = TextAdventureGame()
    game.play()


if __name__ == "__main__":
    main()

import random


class HackerGame:
    def __init__(self):
        self.current_node = "Home"
        self.nodes = {
            "Home": {"data": [], "connections": ["Server A", "Server B"]},
            "Server A": {"data": ["Bank Accounts", "Employee Records"],
                         "connections": ["Home", "Server B", "Firewall"]},
            "Server B": {"data": ["Customer Data", "Product Designs"], "connections": ["Home", "Server A", "Firewall"]},
            "Firewall": {"data": [], "connections": ["Server A", "Server B"]}
        }
        self.player_inventory = []

    def play(self):
        print("Welcome to the Hacker Game!")
        print("You are starting your hacking mission from the 'Home' node.")
        print("Use commands to navigate and retrieve data. Be careful of security!\n")

        while True:
            self.print_node_info()
            command = input("Enter command (hack / move [node] / quit): ").lower().strip()

            if command == "quit":
                print("Exiting game. Goodbye!")
                break
            elif command.startswith("move "):
                destination = command.split(" ")[1].capitalize()
                self.move_to_node(destination)
            elif command == "hack":
                self.hack_node()
            else:
                print("Invalid command! Use 'hack', 'move [node]', or 'quit'.\n")

    def print_node_info(self):
        print(f"Current node: {self.current_node}")
        if self.nodes[self.current_node]["data"]:
            print(f"Data available: {', '.join(self.nodes[self.current_node]['data'])}")
        else:
            print("No data available here.")
        print(f"Connections: {', '.join(self.nodes[self.current_node]['connections'])}\n")

    def move_to_node(self, destination):
        if destination in self.nodes[self.current_node]["connections"]:
            self.current_node = destination
            print(f"Moved to node: {self.current_node}")
        else:
            print(f"Cannot move to {destination}. Not a valid connection.\n")

    def hack_node(self):
        if self.current_node == "Firewall":
            print("You are at the firewall. Hacking attempt failed! Security alert triggered.")
            print("Game over!")
            return

        success_chance = random.randint(1, 10)
        if success_chance <= 7:
            print(f"Hacking attempt successful at {self.current_node}. Data extracted!")
            if self.nodes[self.current_node]["data"]:
                data_found = random.choice(self.nodes[self.current_node]["data"])
                print(f"Extracted: {data_found}")
                self.player_inventory.append(data_found)
                self.nodes[self.current_node]["data"].remove(data_found)
            else:
                print("No data found.")
        else:
            print("Hacking attempt failed! Security alert triggered.")
            print("Game over!")
            return


# Main function to start the game
def main():
    game = HackerGame()
    game.play()


if __name__ == "__main__":
    main()
# ----------------------------------------
import random


class TextAdventureGame:
    def __init__(self):
        self.player_health = 100
        self.player_score = 0
        self.current_room = "Entrance"
        self.player_inventory = []

    def play(self):
        print("Welcome to the Advanced Text Adventure Game!")
        print("You find yourself in a mysterious mansion. Your goal is to explore and find the treasure.\n")

        while self.player_health > 0:
            print(f"Current room: {self.current_room}")
            print(f"Player health: {self.player_health}")
            print(f"Player score: {self.player_score}")
            print(f"Inventory: {', '.join(self.player_inventory)}\n")

            if self.current_room == "Entrance":
                self.room_entrance()
            elif self.current_room == "Living Room":
                self.room_living_room()
            elif self.current_room == "Kitchen":
                self.room_kitchen()
            elif self.current_room == "Bedroom":
                self.room_bedroom()
            elif self.current_room == "Treasure Room":
                self.room_treasure_room()
                break  # End game if player reaches the treasure room
            else:
                print("You are lost in the mansion. Game over!")
                break

    def room_entrance(self):
        print("You are at the entrance of the mansion. There are three doors in front of you.")
        choice = input("Which door do you choose? (left / middle / right): ").lower().strip()

        if choice == "left":
            print("You enter the Living Room.")
            self.current_room = "Living Room"
        elif choice == "middle":
            print("You enter the Kitchen.")
            self.current_room = "Kitchen"
        elif choice == "right":
            print("You enter the Bedroom.")
            self.current_room = "Bedroom"
        else:
            print("Invalid choice. You hesitate and stay at the entrance.")

    def room_living_room(self):
        print("You are in the Living Room. There is a key on the table and a locked door.")
        choice = input("What do you do? (take key / unlock door / go back): ").lower().strip()

        if choice == "take key":
            print("You take the key.")
            self.player_inventory.append("Key")
            self.player_score += 10
            self.room_entrance()  # Return to entrance
        elif choice == "unlock door":
            if "Key" in self.player_inventory:
                print("You unlock the door and find a secret passage to the Treasure Room!")
                self.current_room = "Treasure Room"
            else:
                print("The door is locked. You need a key.")
        elif choice == "go back":
            print("You return to the entrance.")
            self.current_room = "Entrance"
        else:
            print("You ponder your choices in the Living Room.")

    def room_kitchen(self):
        print("You are in the Kitchen. There is a delicious-looking cake on the counter.")
        choice = input("What do you do? (eat cake / ignore cake / go back): ").lower().strip()

        if choice == "eat cake":
            print("The cake was poisoned! You lose 20 health.")
            self.player_health -= 20
            self.room_entrance()  # Return to entrance
        elif choice == "ignore cake":
            print("You resist temptation and go back to the entrance.")
            self.current_room = "Entrance"
        elif choice == "go back":
            print("You return to the entrance.")
            self.current_room = "Entrance"
        else:
            print("You contemplate your options in the Kitchen.")

    def room_bedroom(self):
        print("You are in the Bedroom. There is a chest at the foot of the bed.")
        choice = input("What do you do? (open chest / sleep / go back): ").lower().strip()

        if choice == "open chest":
            print("You find a pile of gold coins! You gain 50 points.")
            self.player_score += 50
            self.player_inventory.append("Gold Coins")
            self.room_entrance()  # Return to entrance
        elif choice == "sleep":
            print("You take a nap and regain some health.")
            self.player_health += 10
            self.room_entrance()  # Return to entrance
        elif choice == "go back":
            print("You return to the entrance.")
            self.current_room = "Entrance"
        else:
            print("You weigh your options in the Bedroom.")

    def room_treasure_room(self):
        print("Congratulations! You found the Treasure Room.")
        print("You have reached the end of the game!\n")
        print(f"Final score: {self.player_score}")
        print(f"Final health: {self.player_health}")


# Main function to start the game
def main():
    game = TextAdventureGame()
    game.play()


if __name__ == "__main__":
    main()



