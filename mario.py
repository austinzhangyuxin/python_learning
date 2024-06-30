import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

# Player settings
player_size = 50
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - player_size]
player_speed = 10
jump_height = 15
gravity = 1

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Simple Mario Game")

# Game variables
is_jumping = False
y_velocity = 0

# Game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get keys
    keys = pygame.key.get_pressed()

    # Move player
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_SPACE] and not is_jumping:
        is_jumping = True
        y_velocity = -jump_height

    # Gravity
    if is_jumping:
        player_pos[1] += y_velocity
        y_velocity += gravity
        if player_pos[1] >= SCREEN_HEIGHT - player_size:
            player_pos[1] = SCREEN_HEIGHT - player_size
            is_jumping = False
            y_velocity = 0

    # Draw player
    pygame.draw.rect(screen, BLUE, (player_pos[0], player_pos[1], player_size, player_size))

    # Refresh screen
    pygame.display.flip()
    pygame.time.Clock().tick(30)
