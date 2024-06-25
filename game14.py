import tkinter as tk
from tkinter import messagebox


class AdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Adventure Game")

        # Game state variables
        self.current_room = "Living Room"
        self.inventory = []

        # Room data
        self.rooms = {
            "Living Room": {
                "description": "You are in the living room. There is a door to the north.",
                "exits": {"north": "Kitchen"},
                "items": ["key"]
            },
            "Kitchen": {
                "description": "You are in the kitchen. There is a door to the south and a door to the east.",
                "exits": {"south": "Living Room", "east": "Bedroom"},
                "items": ["knife"]
            },
            "Bedroom": {
                "description": "You are in the bedroom. There is a door to the west.",
                "exits": {"west": "Kitchen"},
                "items": ["map"]
            }
        }

        # Setup GUI elements
        self.description_label = tk.Label(master, text="", wraplength=300)
        self.description_label.pack(pady=20)

        self.input_frame = tk.Frame(master)
        self.input_frame.pack(pady=10)

        self.command_entry = tk.Entry(self.input_frame, width=30)
        self.command_entry.pack(side=tk.LEFT, padx=5)

        self.submit_button = tk.Button(self.input_frame, text="Submit", command=self.process_command)
        self.submit_button.pack(side=tk.LEFT)

        self.output_label = tk.Label(master, text="", wraplength=300)
        self.output_label.pack(pady=10)

        self.update_room_description()

    def update_room_description(self):
        room = self.rooms[self.current_room]
        self.description_label.config(text=room["description"])
        self.output_label.config(text="Items in room: " + ", ".join(room["items"]))

    def process_command(self):
        command = self.command_entry.get().strip().lower()
        self.command_entry.delete(0, tk.END)

        if command in ["north", "south", "east", "west"]:
            self.move(command)
        elif command == "look":
            self.look()
        elif command.startswith("take "):
            self.take(command.split(" ")[1])
        else:
            messagebox.showerror("Invalid Command",
                                 "Unknown command. Try 'look', 'take <item>', or a direction ('north', 'south', 'east', 'west').")

    def move(self, direction):
        room = self.rooms[self.current_room]
        if direction in room["exits"]:
            self.current_room = room["exits"][direction]
            self.update_room_description()
        else:
            messagebox.showerror("Invalid Move", f"You can't go {direction} from here.")

    def look(self):
        self.update_room_description()

    def take(self, item):
        room = self.rooms[self.current_room]
        if item in room["items"]:
            room["items"].remove(item)
            self.inventory.append(item)
            self.output_label.config(text=f"You took the {item}. Inventory: " + ", ".join(self.inventory))
        else:
            messagebox.showerror("Invalid Item", f"There is no {item} here.")


def main():
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
