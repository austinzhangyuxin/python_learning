import pygame
import random

# Game settings
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 600
GRID_SIZE = 30
COLUMNS = SCREEN_WIDTH // GRID_SIZE
ROWS = SCREEN_HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [
    (0, 255, 255),
    (255, 0, 0),
    (0, 255, 0),
    (255, 255, 0),
    (255, 165, 0),
    (0, 0, 255),
    (128, 0, 128)
]

# Shapes
SHAPES = [
    [[1, 1, 1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 0], [0, 1, 1]],
    [[0, 1, 1], [1, 1, 0]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]]
]


class Tetris:
    def __init__(self):
        self.grid = [[0] * COLUMNS for _ in range(ROWS)]
        self.current_shape = self.new_shape()
        self.current_x = COLUMNS // 2
        self.current_y = 0
        self.game_over = False

    def new_shape(self):
        return random.choice(SHAPES), random.choice(COLORS)

    def draw_grid(self, screen):
        for y in range(ROWS):
            for x in range(COLUMNS):
                if self.grid[y][x] == 0:
                    color = WHITE
                else:
                    color = self.grid[y][x]
                pygame.draw.rect(screen, color, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0)
                pygame.draw.rect(screen, BLACK, (x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1)

    def draw_shape(self, screen):
        shape, color = self.current_shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(
                        screen, color,
                        ((self.current_x + x) * GRID_SIZE, (self.current_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 0
                    )
                    pygame.draw.rect(
                        screen, BLACK,
                        ((self.current_x + x) * GRID_SIZE, (self.current_y + y) * GRID_SIZE, GRID_SIZE, GRID_SIZE), 1
                    )

    def valid_move(self, dx, dy):
        shape, _ = self.current_shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.current_x + x + dx
                    new_y = self.current_y + y + dy
                    if new_x < 0 or new_x >= COLUMNS or new_y >= ROWS or self.grid[new_y][new_x]:
                        return False
        return True

    def freeze_shape(self):
        shape, color = self.current_shape
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[self.current_y + y][self.current_x + x] = color
        self.clear_lines()
        self.current_shape = self.new_shape()
        self.current_x = COLUMNS // 2
        self.current_y = 0
        if not self.valid_move(0, 0):
            self.game_over = True

    def clear_lines(self):
        lines = 0
        for y in range(ROWS - 1, -1, -1):
            if all(self.grid[y]):
                del self.grid[y]
                self.grid.insert(0, [0] * COLUMNS)
                lines += 1

    def move(self, dx, dy):
        if self.valid_move(dx, dy):
            self.current_x += dx
            self.current_y += dy
        elif dy > 0:
            self.freeze_shape()

    def rotate(self):
        shape, color = self.current_shape
        rotated_shape = list(zip(*shape[::-1]))
        if self.valid_move(0, 0):
            self.current_shape = (rotated_shape, color)


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Tetris")
    clock = pygame.time.Clock()
    tetris = Tetris()
    fall_time = 0
    speed = 500

    running = True
    while running:
        screen.fill(BLACK)
        fall_time += clock.get_rawtime()
        clock.tick()

        if fall_time > speed:
            fall_time = 0
            tetris.move(0, 1)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetris.move(-1, 0)
                elif event.key == pygame.K_RIGHT:
                    tetris.move(1, 0)
                elif event.key == pygame.K_DOWN:
                    tetris.move(0, 1)
                elif event.key == pygame.K_UP:
                    tetris.rotate()

        if tetris.game_over:
            print("Game Over!")
            running = False

        tetris.draw_grid(screen)
        tetris.draw_shape(screen)
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()
