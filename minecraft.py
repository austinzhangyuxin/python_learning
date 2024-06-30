import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
GRID_WIDTH = WIDTH // BLOCK_SIZE
GRID_HEIGHT = HEIGHT // BLOCK_SIZE
GROUND_LEVEL = GRID_HEIGHT // 2

# Colors
SKY = (135, 206, 235)
GRASS = (34, 139, 34)
DIRT = (139, 69, 19)
PLAYER = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Advanced Minecraft Game")

# Player setup
player_pos = [GRID_WIDTH // 2, GROUND_LEVEL - 1]
player_speed = 5

# Terrain generation
def generate_terrain():
    terrain = []
    for x in range(GRID_WIDTH):
        column = []
        for y in range(GRID_HEIGHT):
            if y > GROUND_LEVEL:
                column.append(GRASS if random.random() > 0.1 else DIRT)
            else:
                column.append(SKY)
        terrain.append(column)
    return terrain

terrain = generate_terrain()

def draw_terrain():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            color = terrain[x][y]
            pygame.draw.rect(screen, color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def draw_player():
    pygame.draw.rect(screen, PLAYER, (player_pos[0] * BLOCK_SIZE, player_pos[1] * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

def move_player(dx, dy):
    new_x = player_pos[0] + dx
    new_y = player_pos[1] + dy
    if 0 <= new_x < GRID_WIDTH and 0 <= new_y < GRID_HEIGHT:
        if terrain[new_x][new_y] == SKY:
            player_pos[0] = new_x
            player_pos[1] = new_y

# Game loop
running = True
while running:
    screen.fill(SKY)
    draw_terrain()
    draw_player()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        move_player(-1, 0)
    if keys[pygame.K_RIGHT]:
        move_player(1, 0)
    if keys[pygame.K_UP]:
        move_player(0, -1)
    if keys[pygame.K_DOWN]:
        move_player(0, 1)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
