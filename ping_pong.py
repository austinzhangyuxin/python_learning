import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH = 800
HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
FPS = 60

# Game variables
ball_speed = [5, 5]
player_speed = 7
score = [0, 0]

# Create game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Define game objects
player1 = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 60, 10, 120)
player2 = pygame.Rect(10, HEIGHT // 2 - 60, 10, 120)
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and player1.top > 0:
        player1.y -= player_speed
    if keys[pygame.K_DOWN] and player1.bottom < HEIGHT:
        player1.y += player_speed

    # AI movement for player2
    if ball.top < player2.top:
        player2.y -= player_speed
    if ball.bottom > player2.bottom:
        player2.y += player_speed

    # Update ball position
    ball.x += ball_speed[0]
    ball.y += ball_speed[1]

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_speed[1] = -ball_speed[1]

    # Ball collision with players
    if ball.colliderect(player1) or ball.colliderect(player2):
        ball_speed[0] = -ball_speed[0]

    # Ball out of bounds (score update)
    if ball.left <= 0:
        score[1] += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed[0] *= -1
    if ball.right >= WIDTH:
        score[0] += 1
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_speed[0] *= -1

    # Clear screen
    screen.fill(BLACK)

    # Draw players and ball
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)
    pygame.draw.ellipse(screen, WHITE, ball)

    # Draw scores
    font = pygame.font.Font(None, 36)
    text = font.render(f"{score[0]} : {score[1]}", True, WHITE)
    text_rect = text.get_rect(center=(WIDTH // 2, 50))
    screen.blit(text, text_rect)

    # Refresh display
    pygame.display.flip()

    # Cap FPS
    clock.tick(FPS)
