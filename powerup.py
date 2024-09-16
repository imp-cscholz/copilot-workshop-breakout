import pygame
from settings import POWERUP_SIZE, POWERUP_SPEED, YELLOW

class Powerup:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.speed = POWERUP_SPEED

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, YELLOW, self.rect)