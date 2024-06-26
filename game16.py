import tkinter as tk
import random

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 20
BALL_DIAMETER = 30
BALL_SPEED = 5
PADDLE_SPEED = 20

# Create the main window
root = tk.Tk()
root.title("Catch the Ball Game")
canvas = tk.Canvas(root, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg='black')
canvas.pack()

# Create the paddle
paddle = canvas.create_rectangle(WINDOW_WIDTH // 2 - PADDLE_WIDTH // 2, WINDOW_HEIGHT - PADDLE_HEIGHT - 10,
                                 WINDOW_WIDTH // 2 + PADDLE_WIDTH // 2, WINDOW_HEIGHT - 10, fill='white')

# Create the ball
ball = canvas.create_oval(0, 0, BALL_DIAMETER, BALL_DIAMETER, fill='red')
ball_x_speed = BALL_SPEED
ball_y_speed = BALL_SPEED


# Function to move the paddle
def move_paddle(event):
    if event.keysym == 'Left':
        canvas.move(paddle, -PADDLE_SPEED, 0)
    elif event.keysym == 'Right':
        canvas.move(paddle, PADDLE_SPEED, 0)


# Function to update the game
def update_game():
    global ball_x_speed, ball_y_speed

    # Move the ball
    canvas.move(ball, ball_x_speed, ball_y_speed)
    ball_pos = canvas.coords(ball)

    # Bounce off walls
    if ball_pos[0] <= 0 or ball_pos[2] >= WINDOW_WIDTH:
        ball_x_speed = -ball_x_speed
    if ball_pos[1] <= 0:
        ball_y_speed = -ball_y_speed

    # Check if ball hits the paddle
    paddle_pos = canvas.coords(paddle)
    if (ball_pos[2] >= paddle_pos[0] and ball_pos[0] <= paddle_pos[2] and
            ball_pos[3] >= paddle_pos[1] and ball_pos[3] <= paddle_pos[3]):
        ball_y_speed = -ball_y_speed
        canvas.move(ball, 0, -10)

    # Check if ball falls out of the window
    if ball_pos[3] >= WINDOW_HEIGHT:
        canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2, text="Game Over", fill="white",
                           font=("Helvetica", 24))
        return

    root.after(50, update_game)


# Bind the arrow keys to the move_paddle function
root.bind('<Left>', move_paddle)
root.bind('<Right>', move_paddle)

# Start the game
update_game()
root.mainloop()
