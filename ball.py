import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BALL_SIZE, BALL_SPEED_X, BALL_SPEED_Y, WHITE

class Ball:
    def __init__(self):
        self.rect = pygame.Rect((SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2), (BALL_SIZE, BALL_SIZE))
        self.speed_x = BALL_SPEED_X
        self.speed_y = BALL_SPEED_Y

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x = -self.speed_x
        if self.rect.top <= 0:
            self.speed_y = -self.speed_y

    def draw(self, screen):
        pygame.draw.ellipse(screen, WHITE, self.rect)