import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Stunt Cat")

# Cat settings
cat_size = 50
cat_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - cat_size]
cat_speed = 10
jump_height = 20
gravity = 1
is_jumping = False
y_velocity = 0


# Function to draw the cat
def draw_cat(x, y):
    pygame.draw.rect(screen, ORANGE, (x, y, cat_size, cat_size))


# Main game loop
def game_loop():
    global is_jumping, y_velocity

    running = True
    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Get keys
        keys = pygame.key.get_pressed()

        # Move cat
        if keys[pygame.K_LEFT]:
            cat_pos[0] -= cat_speed
        if keys[pygame.K_RIGHT]:
            cat_pos[0] += cat_speed
        if keys[pygame.K_SPACE] and not is_jumping:
            is_jumping = True
            y_velocity = -jump_height

        # Gravity
        if is_jumping:
            cat_pos[1] += y_velocity
            y_velocity += gravity
            if cat_pos[1] >= SCREEN_HEIGHT - cat_size:
                cat_pos[1] = SCREEN_HEIGHT - cat_size
                is_jumping = False
                y_velocity = 0

        # Draw cat
        draw_cat(cat_pos[0], cat_pos[1])

        # Refresh screen
        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
