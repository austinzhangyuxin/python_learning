import tkinter as tk
from tkinter import messagebox


class AdventureGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Adventure Game")

        # Initialize game variables
        self.current_scene = "start"
        self.inventory = []

        # Create a dictionary of scenes
        self.scenes = {
            "start": {
                "text": "Welcome to the Adventure Game!\n\nYou wake up in a mysterious forest. There are paths leading to the north, east, and west. Where do you want to go?",
                "options": {"North": "forest", "East": "river", "West": "cave"}
            },
            "forest": {
                "text": "You are in a dense forest. You hear rustling in the bushes. What do you do?",
                "options": {"Investigate": "treasure", "Go back": "start"}
            },
            "treasure": {
                "text": "You found a hidden treasure chest! Do you want to open it?",
                "options": {"Open": "treasure_opened", "Leave": "forest"}
            },
            "treasure_opened": {
                "text": "Inside the treasure chest, you find a valuable gemstone! You take it with you.",
                "options": {"Continue": "forest"}
            },
            "river": {
                "text": "You arrive at a fast-flowing river. There's a bridge nearby. What will you do?",
                "options": {"Cross the bridge": "village", "Swim across": "river_danger"}
            },
            "river_danger": {
                "text": "The river's current is too strong! You are swept away and wash up downstream. You lose some health.",
                "options": {"Continue": "start"}
            },
            "village": {
                "text": "You reach a peaceful village. The villagers welcome you warmly. You can rest here for a while.",
                "options": {"Rest": "village_rested"}
            },
            "village_rested": {
                "text": "After resting, you feel refreshed and ready to continue your adventure.",
                "options": {"Continue": "start"}
            },
            "cave": {
                "text": "You enter a dark cave. It's too dark to see anything. What will you do?",
                "options": {"Light a torch": "cave_torch", "Leave": "start"}
            },
            "cave_torch": {
                "text": "With the torch lit, you explore deeper into the cave and find a hidden passage.",
                "options": {"Explore": "dragon"}
            },
            "dragon": {
                "text": "You encounter a fearsome dragon guarding a pile of treasure! What do you do?",
                "options": {"Fight": "dragon_defeated", "Sneak past": "start"}
            },
            "dragon_defeated": {
                "text": "With a mighty effort, you defeat the dragon and claim its treasure as your own!",
                "options": {"Continue": "start"}
            }
        }

        # Create widgets
        self.text = tk.Label(master, text=self.scenes[self.current_scene]["text"], wraplength=400, justify=tk.LEFT)
        self.text.pack(padx=10, pady=10)

        self.button_frame = tk.Frame(master)
        self.button_frame.pack(padx=10, pady=10)

        for option in self.scenes[self.current_scene]["options"]:
            tk.Button(self.button_frame, text=option, command=lambda option=option: self.choose_option(option)).pack(
                side=tk.LEFT, padx=5)

    def choose_option(self, option):
        next_scene = self.scenes[self.current_scene]["options"].get(option)

        if next_scene:
            self.current_scene = next_scene
            self.text.config(text=self.scenes[self.current_scene]["text"])
            self.update_buttons()
        else:
            messagebox.showinfo("Game Over", "You cannot go that way.")
            self.current_scene = "start"
            self.text.config(text=self.scenes[self.current_scene]["text"])
            self.update_buttons()

    def update_buttons(self):
        # Clear existing buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

        # Create new buttons for current scene options
        for option in self.scenes[self.current_scene]["options"]:
            tk.Button(self.button_frame, text=option, command=lambda option=option: self.choose_option(option)).pack(
                side=tk.LEFT, padx=5)


def main():
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
