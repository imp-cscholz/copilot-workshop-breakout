import pygame
from settings import SCREEN_WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BRICK_ROWS, BRICK_COLUMNS, RED, GREEN, WHITE

class Brick:
    def __init__(self, x, y, hits=1):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)
        self.hits = hits

    def draw(self, screen):
        color = RED if self.hits == 1 else GREEN
        pygame.draw.rect(screen, WHITE, self.rect)
        inner_rect = self.rect.inflate(-2, -2)
        pygame.draw.rect(screen, color, inner_rect)

def create_bricks():
    bricks = []
    total_bricks_width = BRICK_COLUMNS * BRICK_WIDTH
    horizontal_margin = (SCREEN_WIDTH - total_bricks_width) // 2

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            x = horizontal_margin + col * BRICK_WIDTH
            y = row * BRICK_HEIGHT + 50
            hits = 1 if row % 2 == 0 else 2  # Alternate rows with different hit counts
            brick = Brick(x, y, hits)
            bricks.append(brick)
    return bricks