import pygame
from settings import SCREEN_WIDTH, BRICK_WIDTH, BRICK_HEIGHT, BRICK_ROWS, BRICK_COLUMNS, RED

class Brick:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, screen):
        pygame.draw.rect(screen, RED, self.rect)

def create_bricks():
    bricks = []
    # Calculate the total width of all bricks and the gaps between them
    total_bricks_width = BRICK_COLUMNS * BRICK_WIDTH
    # Calculate the horizontal margin to center the bricks
    horizontal_margin = (SCREEN_WIDTH - total_bricks_width) // 2

    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLUMNS):
            x = horizontal_margin + col * BRICK_WIDTH
            y = row * BRICK_HEIGHT + 50
            brick = Brick(x, y)
            bricks.append(brick)
    return bricks