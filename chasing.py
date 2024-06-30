import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Zombie Chasing Game')

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Player and Zombie settings
PLAYER_SIZE = 30
ZOMBIE_SIZE = 30
PLAYER_SPEED = 5
ZOMBIE_SPEED = 2

# Initial positions
player_pos = [WIDTH // 2, HEIGHT // 2]
zombie_pos = [random.randint(0, WIDTH), random.randint(0, HEIGHT)]

# Game loop
running = True
clock = pygame.time.Clock()

def move_zombie(player_pos, zombie_pos):
    dx = player_pos[0] - zombie_pos[0]
    dy = player_pos[1] - zombie_pos[1]
    dist = math.sqrt(dx**2 + dy**2)
    if dist != 0:
        dx = dx / dist
        dy = dy / dist
    zombie_pos[0] += dx * ZOMBIE_SPEED
    zombie_pos[1] += dy * ZOMBIE_SPEED

while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= PLAYER_SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < WIDTH - PLAYER_SIZE:
        player_pos[0] += PLAYER_SPEED
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= PLAYER_SPEED
    if keys[pygame.K_DOWN] and player_pos[1] < HEIGHT - PLAYER_SIZE:
        player_pos[1] += PLAYER_SPEED

    move_zombie(player_pos, zombie_pos)

    # Draw player and zombie
    pygame.draw.rect(screen, WHITE, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))
    pygame.draw.rect(screen, RED, (zombie_pos[0], zombie_pos[1], ZOMBIE_SIZE, ZOMBIE_SIZE))

    # Check collision
    if (zombie_pos[0] < player_pos[0] < zombie_pos[0] + ZOMBIE_SIZE or
        zombie_pos[0] < player_pos[0] + PLAYER_SIZE < zombie_pos[0] + ZOMBIE_SIZE) and \
       (zombie_pos[1] < player_pos[1] < zombie_pos[1] + ZOMBIE_SIZE or
        zombie_pos[1] < player_pos[1] + PLAYER_SIZE < zombie_pos[1] + ZOMBIE_SIZE):
        font = pygame.font.Font(None, 74)
        text = font.render('Game Over', True, WHITE)
        screen.blit(text, (WIDTH//2 - 150, HEIGHT//2 - 37))
        pygame.display.flip()
        pygame.time.wait(2000)
        running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
