import tkinter as tk
import math
import random

class AsteroidsGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Asteroids Game")

        self.canvas = tk.Canvas(self.root, width=800, height=600, bg='black')
        self.canvas.pack()

        self.player = self.canvas.create_polygon(400, 300, 380, 320, 420, 320, fill='blue')
        self.player_angle = 0
        self.player_speed = 0
        self.player_x = 400
        self.player_y = 300

        self.bullets = []

        self.root.bind('<KeyPress>', self.key_press)
        self.root.bind('<KeyRelease>', self.key_release)

        self.run_game()

    def run_game(self):
        self.move_player()
        self.move_bullets()
        self.check_collisions()
        self.spawn_asteroid()
        self.root.after(30, self.run_game)  # Run every 30 milliseconds

    def move_player(self):
        dx = math.cos(math.radians(self.player_angle)) * self.player_speed
        dy = -math.sin(math.radians(self.player_angle)) * self.player_speed
        self.player_x += dx
        self.player_y += dy

        self.canvas.coords(self.player,
                           self.player_x, self.player_y,
                           self.player_x + 20, self.player_y + 20,
                           self.player_x - 20, self.player_y + 20)

        self.player_x %= 800
        self.player_y %= 600

    def move_bullets(self):
        new_bullets = []
        for bullet in self.bullets:
            x, y = self.canvas.coords(bullet)
            self.canvas.move(bullet, 10, 0)
            if x < 0 or x > 800 or y < 0 or y > 600:
                self.canvas.delete(bullet)
            else:
                new_bullets.append(bullet)
        self.bullets = new_bullets

    def spawn_asteroid(self):
        if random.random() < 0.02:  # Adjust this probability for asteroid spawn rate
            asteroid_x = random.randint(0, 800)
            asteroid = self.canvas.create_oval(asteroid_x, -50, asteroid_x + 50, 0, outline='white')
            self.move_asteroid(asteroid)

    def move_asteroid(self, asteroid):
        self.canvas.move(asteroid, 0, 5)
        x1, y1, x2, y2 = self.canvas.coords(asteroid)
        if y2 > 600:
            self.canvas.delete(asteroid)
        else:
            self.root.after(30, lambda: self.move_asteroid(asteroid))

    def check_collisions(self):
        player_bbox = self.canvas.bbox(self.player)
        for asteroid in self.canvas.find_all():
            if asteroid != self.player and self.canvas.bbox(asteroid) and self.canvas.bbox(asteroid) != player_bbox:
                if self.canvas.bbox(asteroid) and self.canvas.bbox(asteroid) == player_bbox:
                    self.game_over()
                for bullet in self.bullets:
                    if self.canvas.bbox(asteroid) and self.canvas.bbox(asteroid) == self.canvas.bbox(bullet):
                        self.canvas.delete(asteroid)
                        self.canvas.delete(bullet)

    def key_press(self, event):
        if event.keysym == 'Up':
            self.player_speed = 5
        elif event.keysym == 'Left':
            self.player_angle -= 10
        elif event.keysym == 'Right':
            self.player_angle += 10
        elif event.keysym == 'space':
            x1, y1, x2, y2 = self.canvas.coords(self.player)
            bullet = self.canvas.create_oval(x1 + 10, y1 - 10, x2 - 10, y1, fill='yellow')
            self.bullets.append(bullet)

    def key_release(self, event):
        if event.keysym == 'Up':
            self.player_speed = 0

    def game_over(self):
        self.canvas.delete(tk.ALL)
        self.canvas.create_text(400, 300, text="Game Over", font=('Arial', 40), fill='red')


def main():
    root = tk.Tk()
    game = AsteroidsGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
