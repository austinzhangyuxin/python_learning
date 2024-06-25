import tkinter as tk
from tkinter import messagebox


class AdventureGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Adventure Game")

        # Game variables
        self.story_index = 0
        self.story = [
            "You wake up in a mysterious forest. What do you do?",
            "You see a path leading deeper into the forest. Do you follow it?",
            "You encounter a river. Do you swim across or find another way around?"
        ]
        self.choices = [
            ["Explore the forest", "Stay put and observe"],
            ["Follow the path", "Go back where you came from"],
            ["Swim across", "Look for a bridge"]
        ]

        # Create GUI elements
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.root, text=self.story[self.story_index])
        self.label.pack(pady=10)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        for i, choice in enumerate(self.choices[self.story_index]):
            btn = tk.Button(self.button_frame, text=choice, width=20, command=lambda c=i: self.next_story(c))
            btn.grid(row=0, column=i, padx=5, pady=5)

    def next_story(self, choice_index):
        if self.story_index == len(self.story) - 1:
            messagebox.showinfo("End of Game", "You have reached the end of the adventure!")
            self.root.destroy()
            return

        self.story_index += 1
        self.label.config(text=self.story[self.story_index])

        self.button_frame.destroy()
        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack(pady=10)

        for i, choice in enumerate(self.choices[self.story_index]):
            btn = tk.Button(self.button_frame, text=choice, width=20, command=lambda c=i: self.next_story(c))
            btn.grid(row=0, column=i, padx=5, pady=5)


def main():
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
