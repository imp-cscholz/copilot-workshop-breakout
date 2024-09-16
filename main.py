import pygame
import sys
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, BLACK, WHITE
from paddle import Paddle
from ball import Ball
from brick import create_bricks

def draw_text(screen, text, size, color, x, y):
    font = pygame.font.Font(None, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Breakout Game")
    clock = pygame.time.Clock()

    paddle = Paddle()
    ball = Ball()
    bricks = create_bricks()
    running = True
    game_state = "start"  # Possible states: start, playing, win, lose

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_SPACE and game_state == "start":
                    game_state = "playing"
                if event.key == pygame.K_SPACE and (game_state == "win" or game_state == "lose"):
                    game_state = "start"
                    ball = Ball()
                    bricks = create_bricks()

        if game_state == "playing":
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move(-paddle.speed)
            if keys[pygame.K_RIGHT]:
                paddle.move(paddle.speed)

            ball.move()

            # Collision with paddle
            if ball.rect.colliderect(paddle.rect):
                offset = (ball.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
                ball.speed_y = -ball.speed_y
                ball.speed_x = ball.speed_x + offset * 5

            # Collision with bricks
            for brick in bricks[:]:
                if ball.rect.colliderect(brick.rect):
                    ball.speed_y = -ball.speed_y
                    bricks.remove(brick)

            # Check if the ball has fallen below the paddle
            if ball.rect.top > SCREEN_HEIGHT:
                game_state = "lose"

            # Check if all bricks have been destroyed
            if not bricks:
                game_state = "win"

        screen.fill(BLACK)

        if game_state == "start":
            draw_text(screen, "Press SPACE to Start", 50, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif game_state == "win":
            draw_text(screen, "You Win! Press SPACE to Restart", 50, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif game_state == "lose":
            draw_text(screen, "You Lose! Press SPACE to Restart", 50, WHITE, SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        elif game_state == "playing":
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