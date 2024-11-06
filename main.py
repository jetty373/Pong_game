# main.py

import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100
PADDLE_SPEED = 5

# Ball settings
BALL_SIZE = 20
BALL_SPEED_X = 4
BALL_SPEED_Y = 4

# Player and AI paddle positions
player_paddle = pygame.Rect(WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
ai_paddle = pygame.Rect(20, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Ball position and speed
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_speed_x = BALL_SPEED_X
ball_speed_y = BALL_SPEED_Y

# Game loop
def main():
    clock = pygame.time.Clock()
    running = True
    player_score = 0
    ai_score = 0
    font = pygame.font.Font(None, 36)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Player paddle movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_paddle.top > 0:
            player_paddle.y -= PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_paddle.bottom < HEIGHT:
            player_paddle.y += PADDLE_SPEED

        # AI paddle movement
        if ai_paddle.centery < ball.centery:
            ai_paddle.y += PADDLE_SPEED
        elif ai_paddle.centery > ball.centery:
            ai_paddle.y -= PADDLE_SPEED

        # Ball movement
        ball.x += ball_speed_x
        ball.y += ball_speed_y

        # Ball collision with top/bottom walls
        if ball.top <= 0 or ball.bottom >= HEIGHT:
            ball_speed_y *= -1

        # Ball collision with paddles
        if ball.colliderect(player_paddle) or ball.colliderect(ai_paddle):
            ball_speed_x *= -1

        # Scoring
        if ball.left <= 0:
            player_score += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball_speed_x *= -1
        if ball.right >= WIDTH:
            ai_score += 1
            ball.x, ball.y = WIDTH // 2, HEIGHT // 2
            ball_speed_x *= -1

        # Drawing
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, player_paddle)
        pygame.draw.rect(screen, WHITE, ai_paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))

        # Display scores
        player_text = font.render(f"{player_score}", True, WHITE)
        ai_text = font.render(f"{ai_score}", True, WHITE)
        screen.blit(player_text, (WIDTH - 60, 20))
        screen.blit(ai_text, (40, 20))

        pygame.display.flip()
        clock.tick(60)

if __name__ == "__main__":
    main()
