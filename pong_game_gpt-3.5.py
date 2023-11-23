import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Pong Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle dimensions
paddle_width = 10
paddle_height = 100

# Create the paddles
player1_paddle = pygame.Rect(50, window_height//2 - paddle_height//2, paddle_width, paddle_height)
player2_paddle = pygame.Rect(window_width - 50 - paddle_width, window_height//2 - paddle_height//2, paddle_width, paddle_height)

# Paddle movement speed
paddle_speed = 5

# Ball dimensions and speed
ball = pygame.Rect(window_width//2 - 15, window_height//2 - 15, 30, 30)
ball_speed_x = 7
ball_speed_y = 7

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Paddle movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player1_paddle.y -= paddle_speed
    if keys[pygame.K_s]:
        player1_paddle.y += paddle_speed
    if keys[pygame.K_UP]:
        player2_paddle.y -= paddle_speed
    if keys[pygame.K_DOWN]:
        player2_paddle.y += paddle_speed

    # Ball movement
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with walls
    if ball.top <= 0 or ball.bottom >= window_height:
        ball_speed_y *= -1
    if ball.left <= 0 or ball.right >= window_width:
        ball_speed_x *= -1

    # Ball collision with paddles
    if ball.colliderect(player1_paddle) or ball.colliderect(player2_paddle):
        ball_speed_x *= -1

    # Draw everything
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, player1_paddle)
    pygame.draw.rect(window, WHITE, player2_paddle)
    pygame.draw.ellipse(window, WHITE, ball)
    pygame.draw.aaline(window, WHITE, (window_width//2, 0), (window_width//2, window_height))

    # Update the display
    pygame.display.flip()