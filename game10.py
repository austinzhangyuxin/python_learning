import tkinter as tk
import random


class RobotGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot Game")
        self.master.geometry("600x600")

        # Game constants
        self.GRID_SIZE = 30  # Size of each grid cell in pixels
        self.GRID_WIDTH = 40  # Number of grid cells horizontally
        self.GRID_HEIGHT = 30  # Number of grid cells vertically

        # Create canvas
        self.canvas = tk.Canvas(master, width=self.GRID_WIDTH * self.GRID_SIZE, height=self.GRID_HEIGHT * self.GRID_SIZE, bg='white')
        self.canvas.pack()

        # Initialize game state
        self.robot_x = random.randint(0, self.GRID_WIDTH - 1)
        self.robot_y = random.randint(0, self.GRID_HEIGHT - 1)
        self.goal_x = random.randint(0, self.GRID_WIDTH - 1)
        self.goal_y = random.randint(0, self.GRID_HEIGHT - 1)
        while self.goal_x == self.robot_x and self.goal_y == self.robot_y:
            self.goal_x = random.randint(0, self.GRID_WIDTH - 1)
            self.goal_y = random.randint(0, self.GRID_HEIGHT - 1)

        self.obstacles = []
        self.generate_obstacles()

        self.draw_game()

        # Bind arrow key events
        self.master.bind("<KeyPress>", self.key_press_handler)

    def draw_game(self):
        self.canvas.delete("all")

        # Draw robot
        robot_size = self.GRID_SIZE // 2
        self.robot = self.canvas.create_rectangle(self.robot_x * self.GRID_SIZE + 5, self.robot_y * self.GRID_SIZE + 5,
                                                  (self.robot_x + 1) * self.GRID_SIZE - 5, (self.robot_y + 1) * self.GRID_SIZE - 5,
                                                  fill='blue')

        # Draw goal
        self.goal = self.canvas.create_rectangle(self.goal_x * self.GRID_SIZE + 10, self.goal_y * self.GRID_SIZE + 10,
                                                 (self.goal_x + 1) * self.GRID_SIZE - 10, (self.goal_y + 1) * self.GRID_SIZE - 10,
                                                 fill='green')

        # Draw obstacles
        for obstacle in self.obstacles:
            self.canvas.create_rectangle(obstacle[0] * self.GRID_SIZE, obstacle[1] * self.GRID_SIZE,
                                         (obstacle[0] + 1) * self.GRID_SIZE, (obstacle[1] + 1) * self.GRID_SIZE,
                                         fill='red')

    def generate_obstacles(self):
        num_obstacles = random.randint(10, 20)
        for _ in range(num_obstacles):
            x = random.randint(0, self.GRID_WIDTH - 1)
            y = random.randint(0, self.GRID_HEIGHT - 1)
            if (x, y) != (self.robot_x, self.robot_y) and (x, y) != (self.goal_x, self.goal_y):
                self.obstacles.append((x, y))

    def key_press_handler(self, event):
        key = event.keysym
        if key == "Up" and self.robot_y > 0:
            if (self.robot_x, self.robot_y - 1) not in self.obstacles:
                self.robot_y -= 1
        elif key == "Down" and self.robot_y < self.GRID_HEIGHT - 1:
            if (self.robot_x, self.robot_y + 1) not in self.obstacles:
                self.robot_y += 1
        elif key == "Left" and self.robot_x > 0:
            if (self.robot_x - 1, self.robot_y) not in self.obstacles:
                self.robot_x -= 1
        elif key == "Right" and self.robot_x < self.GRID_WIDTH - 1:
            if (self.robot_x + 1, self.robot_y) not in self.obstacles:
                self.robot_x += 1

        self.check_goal_reached()
        self.draw_game()

    def check_goal_reached(self):
        if self.robot_x == self.goal_x and self.robot_y == self.goal_y:
            self.canvas.create_text(self.GRID_WIDTH * self.GRID_SIZE // 2, self.GRID_HEIGHT * self.GRID_SIZE // 2,
                                    text="Goal Reached!", font=("Helvetica", 24), fill="black")


def main():
    root = tk.Tk()
    game = RobotGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
