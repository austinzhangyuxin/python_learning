import tkinter as tk
import random
import time


class DinoGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Dino Game")

        self.canvas = tk.Canvas(self.root, width=800, height=400, bg='white')
        self.canvas.pack()

        self.dino = self.canvas.create_rectangle(50, 350, 100, 400, fill='green')
        self.obstacle = None

        self.jump_speed = 3
        self.gravity = 0.5
        self.jump_count = 0
        self.jumping = False

        self.score = 0
        self.score_label = self.canvas.create_text(700, 50, text=f"Score: {self.score}", font=('Arial', 20), anchor='e')

        self.root.bind('<space>', self.jump)

        self.run_game()

    def jump(self, event):
        if not self.jumping:
            self.jumping = True
            self.jump_count = 20

    def run_game(self):
        if self.jumping:
            self.jump_dino()

        if self.obstacle is None:
            self.create_obstacle()

        self.move_obstacle()

        if self.detect_collision():
            self.game_over()

        self.canvas.after(20, self.run_game)

    def jump_dino(self):
        if self.jump_count >= -20:
            self.canvas.move(self.dino, 0, -self.jump_count)
            self.jump_count -= 1
        else:
            self.jumping = False

    def create_obstacle(self):
        x = 800
        y = random.randint(300, 380)
        self.obstacle = self.canvas.create_rectangle(x, y, x + 20, y + 20, fill='red')

    def move_obstacle(self):
        self.canvas.move(self.obstacle, -5, 0)
        if self.canvas.coords(self.obstacle)[2] < 0:
            self.canvas.delete(self.obstacle)
            self.obstacle = None
            self.score += 1
            self.canvas.itemconfig(self.score_label, text=f"Score: {self.score}")

    def detect_collision(self):
        dino_coords = self.canvas.coords(self.dino)
        obstacle_coords = self.canvas.coords(self.obstacle) if self.obstacle else []

        if obstacle_coords and self.is_collision(dino_coords, obstacle_coords):
            return True

        return False

    def is_collision(self, dino_coords, obstacle_coords):
        x1, y1, x2, y2 = dino_coords
        x3, y3, x4, y4 = obstacle_coords
        if (x2 >= x3 and y2 >= y3) and (x4 >= x1 and y4 >= y1):
            return True
        return False

    def game_over(self):
        self.canvas.create_text(400, 200, text="Game Over", font=('Arial', 40), fill='red')
        self.canvas.create_text(400, 250, text=f"Final Score: {self.score}", font=('Arial', 30), fill='black')

        self.canvas.unbind('<space>')
        self.root.after_cancel(self.run_game)


def main():
    root = tk.Tk()
    game = DinoGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
