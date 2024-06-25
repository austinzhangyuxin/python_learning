import tkinter as tk
import random


class ZombieShootingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Zombie Shooting Game")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.player = self.canvas.create_oval(390, 290, 410, 310, fill='blue')  # Player crosshair
        self.zombies = []

        self.canvas.bind('<Button-1>', self.shoot_zombie)

        self.run_game()

    def run_game(self):
        self.create_zombie()
        self.move_zombies()
        self.check_collision()
        self.root.after(1000, self.run_game)  # Run every second

    def create_zombie(self):
        zombie_size = random.randint(20, 40)
        zombie_x = random.randint(50, 750)
        zombie_y = random.randint(50, 550)
        zombie = self.canvas.create_rectangle(zombie_x, zombie_y,
                                             zombie_x + zombie_size, zombie_y + zombie_size,
                                             fill='green')
        self.zombies.append(zombie)

    def move_zombies(self):
        for zombie in self.zombies:
            dx = random.randint(-5, 5)
            dy = random.randint(-5, 5)
            self.canvas.move(zombie, dx, dy)

    def shoot_zombie(self, event):
        x, y = event.x, event.y
        zombie_hit = self.canvas.find_closest(x, y)
        if zombie_hit:
            self.canvas.delete(zombie_hit[0])
            self.zombies.remove(zombie_hit[0])

    def check_collision(self):
        player_coords = self.canvas.coords(self.player)
        player_center_x = (player_coords[0] + player_coords[2]) / 2
        player_center_y = (player_coords[1] + player_coords[3]) / 2

        for zombie in self.zombies:
            zombie_coords = self.canvas.coords(zombie)
            zombie_center_x = (zombie_coords[0] + zombie_coords[2]) / 2
            zombie_center_y = (zombie_coords[1] + zombie_coords[3]) / 2

            if (abs(player_center_x - zombie_center_x) < 20 and
                abs(player_center_y - zombie_center_y) < 20):
                self.game_over()

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(400, 300, text="Game Over", font=('Arial', 40), fill='red')


def main():
    root = tk.Tk()
    game = ZombieShootingGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
