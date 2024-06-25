import tkinter as tk
import random


class ClickGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Click Game")
        self.canvas = tk.Canvas(root, width=400, height=400, bg='white')
        self.canvas.pack()
        self.score = 0
        self.score_label = tk.Label(root, text=f"Score: {self.score}")
        self.score_label.pack()
        self.circles = []
        self.spawn_circle()

    def spawn_circle(self):
        x = random.randint(50, 350)
        y = random.randint(50, 350)
        circle = self.canvas.create_oval(x, y, x+50, y+50, fill='blue')
        self.circles.append(circle)
        self.move_circle(circle)

    def move_circle(self, circle):
        dx = random.choice([-10, -5, 5, 10])
        dy = random.choice([-10, -5, 5, 10])
        self.canvas.move(circle, dx, dy)
        self.root.after(100, lambda: self.move_circle(circle))
        self.check_collision(circle)

    def check_collision(self, circle):
        x1, y1, x2, y2 = self.canvas.coords(circle)
        overlaps = self.canvas.find_overlapping(x1, y1, x2, y2)
        if len(overlaps) > 1:
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.canvas.delete(circle)
            self.circles.remove(circle)
            self.spawn_circle()


def main():
    root = tk.Tk()
    game = ClickGame(root)
    root.mainloop()


if __name__ == "__main__":
    main()
