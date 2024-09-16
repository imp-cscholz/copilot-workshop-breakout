import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT, PADDLE_SPEED, WHITE

class Paddle:
    def __init__(self):
        self.rect = pygame.Rect((SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - 30), (PADDLE_WIDTH, PADDLE_HEIGHT))
        self.speed = PADDLE_SPEED

    def move(self, dx):
        self.rect.x += dx
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)