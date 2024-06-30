import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 60
PLAYER_SPEED = 5

# Bullet settings
BULLET_WIDTH = 5
BULLET_HEIGHT = 10
BULLET_SPEED = 7

# Enemy settings
ENEMY_WIDTH = 50
ENEMY_HEIGHT = 50
ENEMY_SPEED = 3

# Setup screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Shooting Game")

# Clock to control frame rate
clock = pygame.time.Clock()


class Player:
    def __init__(self):
        self.x = SCREEN_WIDTH // 2
        self.y = SCREEN_HEIGHT - PLAYER_HEIGHT
        self.width = PLAYER_WIDTH
        self.height = PLAYER_HEIGHT
        self.color = WHITE
        self.speed = PLAYER_SPEED
        self.bullets = []

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self, dx):
        self.x += dx
        self.x = max(0, min(self.x, SCREEN_WIDTH - self.width))

    def shoot(self):
        bullet = Bullet(self.x + self.width // 2, self.y)
        self.bullets.append(bullet)


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = BULLET_WIDTH
        self.height = BULLET_HEIGHT
        self.color = RED
        self.speed = BULLET_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y -= self.speed


class Enemy:
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)
        self.y = random.randint(-100, -40)
        self.width = ENEMY_WIDTH
        self.height = ENEMY_HEIGHT
        self.color = WHITE
        self.speed = ENEMY_SPEED

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

    def move(self):
        self.y += self.speed
        if self.y > SCREEN_HEIGHT:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, SCREEN_WIDTH - ENEMY_WIDTH)


def main():
    player = Player()
    enemies = [Enemy() for _ in range(5)]
    running = True

    while running:
        screen.fill(BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player.move(-player.speed)
        if keys[pygame.K_RIGHT]:
            player.move(player.speed)
        if keys[pygame.K_SPACE]:
            player.shoot()

        for bullet in player.bullets[:]:
            bullet.move()
            if bullet.y < 0:
                player.bullets.remove(bullet)

        for enemy in enemies:
            enemy.move()
            for bullet in player.bullets:
                if bullet.x < enemy.x + enemy.width and bullet.x + bullet.width > enemy.x and bullet.y < enemy.y + enemy.height and bullet.y + bullet.height > enemy.y:
                    enemies.remove(enemy)
                    player.bullets.remove(bullet)
                    break

        player.draw()
        for bullet in player.bullets:
            bullet.draw()
        for enemy in enemies:
            enemy.draw()

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
