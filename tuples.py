import tkinter as tk
import random


class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Collect Items Game")
        self.canvas_width = 400
        self.canvas_height = 400
        self.cell_size = 40
        self.rows = self.canvas_height // self.cell_size
        self.cols = self.canvas_width // self.cell_size
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack()

        self.items = []
        self.player = (0, 0)  # Initial position of the player

        self.create_board()
        self.generate_items()
        self.draw_board()

        self.master.bind("<KeyPress>", self.key_press_handler)

    def create_board(self):
        # Create grid lines
        for i in range(0, self.canvas_width, self.cell_size):
            self.canvas.create_line(i, 0, i, self.canvas_height, fill='gray', width=1)
        for j in range(0, self.canvas_height, self.cell_size):
            self.canvas.create_line(0, j, self.canvas_width, j, fill='gray', width=1)

    def generate_items(self):
        num_items = random.randint(5, 10)
        for _ in range(num_items):
            item_x = random.randint(0, self.cols - 1)
            item_y = random.randint(0, self.rows - 1)
            self.items.append((item_x, item_y))

    def draw_board(self):
        self.canvas.delete("items")
        for item in self.items:
            item_x, item_y = item
            x1 = item_x * self.cell_size
            y1 = item_y * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            self.canvas.create_rectangle(x1, y1, x2, y2, fill='orange', tags="items")

        player_x, player_y = self.player
        px1 = player_x * self.cell_size
        py1 = player_y * self.cell_size
        px2 = px1 + self.cell_size
        py2 = py1 + self.cell_size
        self.canvas.create_rectangle(px1, py1, px2, py2, fill='blue', tags="player")

    def key_press_handler(self, event):
        key = event.keysym
        player_x, player_y = self.player
        if key == "Up" and player_y > 0:
            self.player = (player_x, player_y - 1)
        elif key == "Down" and player_y < self.rows - 1:
            self.player = (player_x, player_y + 1)
        elif key == "Left" and player_x > 0:
            self.player = (player_x - 1, player_y)
        elif key == "Right" and player_x < self.cols - 1:
            self.player = (player_x + 1, player_y)

        self.check_item_collection()
        self.draw_board()

    def check_item_collection(self):
        player_x, player_y = self.player
        if (player_x, player_y) in self.items:
            self.items.remove((player_x, player_y))
            if not self.items:
                self.canvas.create_text(self.canvas_width // 2, self.canvas_height // 2,
                                        text="You collected all items!", font=("Helvetica", 24), fill="black")


# -----------------------------
def main():
    root = tk.Tk()
    game = Game(root)
    root.mainloop()


if __name__ == "__main__":
    main()

# Creating tuples
empty_tuple = ()  # Empty tuple
single_element_tuple = (1,)  # Tuple with a single element (note the comma)
fruits = ('apple', 'banana', 'cherry')  # Tuple with multiple elements
person = ('John', 25, 'john@example.com')  # Tuple with heterogeneous elements
nested_tuple = ('a', (1, 2, 3), ('x', 'y', 'z'))  # Nested tuple

# Accessing elements of a tuple
print(fruits[0])  # Output: 'apple'
print(person[1])  # Output: 25
print(nested_tuple[1][2])  # Output: 3 (accessing nested tuple element)

# Tuple slicing
numbers = (1, 2, 3, 4, 5)
print(numbers[1:4])  # Output: (2, 3, 4)

# Concatenating tuples
tuple1 = ('a', 'b', 'c')
tuple2 = ('x', 'y', 'z')
concatenated_tuple = tuple1 + tuple2
print(concatenated_tuple)  # Output: ('a', 'b', 'c', 'x', 'y', 'z')

# Repetition in tuples
repeated_tuple = tuple1 * 3
print(repeated_tuple)  # Output: ('a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c')

# Tuple methods
numbers = (1, 2, 3, 4, 2, 2)
print(numbers.count(2))  # Output: 3 (count occurrences of 2)
print(numbers.index(4))  # Output: 3 (find index of first occurrence of 4)


# Use case: Returning multiple values from a function
def get_coordinates():
    x = 10
    y = 20
    return x, y  # Returning as a tuple


x, y = get_coordinates()
print(f"X: {x}, Y: {y}")  # Output: X: 10, Y: 20

# Create a tuple containing four items: 9, 11, 15, and 17
odd_numbers = (9, 11, 15, 17)

# Print the third item of the tuple (using a positive index)
print(odd_numbers[2])  # Output: 15
