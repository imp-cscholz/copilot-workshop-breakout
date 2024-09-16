import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK
from paddle import Paddle
from ball import Ball
from brick import create_bricks

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout Game")
    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            paddle.move(-paddle.speed)
        if keys[pygame.K_RIGHT]:
            paddle.move(paddle.speed)

        ball.move()

        # Collision with paddle
        if ball.rect.colliderect(paddle.rect):
            ball.speed_y = -ball.speed_y

        # Collision with bricks
        for brick in bricks[:]:
            if ball.rect.colliderect(brick.rect):
                ball.speed_y = -ball.speed_y
                bricks.remove(brick)

        # Check if the ball has fallen below the paddle
        if ball.rect.top > SCREEN_HEIGHT:
            running = False

        # Check if all bricks have been destroyed
        if not bricks:
            running = False

        screen.fill(BLACK)
        paddle.draw(screen)
        ball.draw(screen)
        for brick in bricks:
            brick.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()