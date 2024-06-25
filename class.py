class ToyRobot:
    # This is a class variable. All toy robots are blue.
    color = input("color: ")

    def __init__(self, name):
        # This is an instance variable. Each toy robot has a unique name.
        self.name = name


robot1 = ToyRobot("Robo1")
robot2 = ToyRobot("Robo2")

print(robot1.name)  # This will print: Robo1
print(robot2.name)  # This will print: Robo2

print(robot1.color)  # This will print: blue
print(robot2.color)  # This will print: blue


# -----------------------
class Character:
    # Class variables
    grid_size = 5
    goal_position = (4, 4)

    def __init__(self, name):
        # Instance variables
        self.name = name
        self.position = (0, 0)

    def move_up(self):
        x, y = self.position
        if x > 0:
            self.position = (x - 1, y)

    def move_down(self):
        x, y = self.position
        if x < self.grid_size - 1:
            self.position = (x + 1, y)

    def move_left(self):
        x, y = self.position
        if y > 0:
            self.position = (x, y - 1)

    def move_right(self):
        x, y = self.position
        if y < self.grid_size - 1:
            self.position = (x, y + 1)

    def has_reached_goal(self):
        return self.position == self.goal_position

    def print_position(self):
        print(f"{self.name} is at position {self.position}")


def play_game():
    character = Character("Player1")
    print("Welcome to the grid game!")
    print("Your goal is to reach the position (4, 4).")
    character.print_position()

    while not character.has_reached_goal():
        move = input("Enter your move (up, down, left, right): ").strip().lower()

        if move == "up":
            character.move_up()
        elif move == "down":
            character.move_down()
        elif move == "left":
            character.move_left()
        elif move == "right":
            character.move_right()
        else:
            print("Invalid move. Please enter 'up', 'down', 'left', or 'right'.")

        character.print_position()

    print(f"Congratulations, {character.name}! You have reached the goal at {character.goal_position}!")


if __name__ == "__main__":
    play_game()
