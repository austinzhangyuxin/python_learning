import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sun Cat")


# Function to draw the sun
def draw_sun():
    pygame.draw.circle(screen, YELLOW, (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), 100)


# Function to draw the cat
def draw_cat(x, y):
    # Body
    pygame.draw.rect(screen, ORANGE, (x, y, 100, 50))
    # Head
    pygame.draw.circle(screen, ORANGE, (x + 120, y + 25), 25)
    # Eyes
    pygame.draw.circle(screen, BLACK, (x + 110, y + 20), 5)
    pygame.draw.circle(screen, BLACK, (x + 130, y + 20), 5)
    # Ears
    pygame.draw.polygon(screen, ORANGE, [(x + 110, y), (x + 100, y - 20), (x + 120, y)])
    pygame.draw.polygon(screen, ORANGE, [(x + 130, y), (x + 120, y - 20), (x + 140, y)])
    # Tail
    pygame.draw.line(screen, ORANGE, (x - 20, y + 25), (x - 50, y + 10), 10)


# Main game loop
def game_loop():
    x = SCREEN_WIDTH // 2 - 50
    y = SCREEN_HEIGHT // 2 + 100
    running = True

    while running:
        screen.fill(WHITE)
        draw_sun()
        draw_cat(x, y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        pygame.time.Clock().tick(30)

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    game_loop()
