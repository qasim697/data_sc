


### Bricks Game Code




import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Paddle properties
PADDLE_WIDTH = 200
PADDLE_HEIGHT = 15
PADDLE_SPEED = 10

# Ball properties
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = -5

# Brick properties
BRICK_WIDTH = 75
BRICK_HEIGHT = 20
BRICK_ROWS = 5
BRICK_COLS = 10

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Bricks Game")

# Function to create bricks
def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick_rect = pygame.Rect(col * (BRICK_WIDTH + 5) + 50, 
                                      row * (BRICK_HEIGHT + 5) + 50, 
                                      BRICK_WIDTH, 
                                      BRICK_HEIGHT)
            bricks.append(brick_rect)
    return bricks

# Main function
def main():
    running = True
    clock = pygame.time.Clock()
    
    paddle = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, 
                         SCREEN_HEIGHT - PADDLE_HEIGHT - 10, 
                         PADDLE_WIDTH, 
                         PADDLE_HEIGHT)

    ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
    ball_speed_x = BALL_SPEED_X
    ball_speed_y = BALL_SPEED_Y

    bricks = create_bricks()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle.left > 0:
            paddle.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and paddle.right < SCREEN_WIDTH:
            paddle.x += PADDLE_SPEED
        
        # Move the ball
        ball.x += ball_speed_x
        ball.y += ball_speed_y
        
        # Check for ball collisions
        if ball.left <= 0 or ball.right >= SCREEN_WIDTH:
            ball_speed_x *= -1  # Bounce off left/right walls
        if ball.top <= 0:
            ball_speed_y *= -1  # Bounce off top wall
        if ball.colliderect(paddle):
            ball_speed_y *= -1  # Bounce off the paddle
        if ball.bottom >= SCREEN_HEIGHT:
            running = False  # Game over

        # Check brick collisions
        for brick in bricks:
            if ball.colliderect(brick):
                ball_speed_y *= -1
                bricks.remove(brick)  # Remove the brick
                break

        # Fill the screen with white background
        screen.fill(WHITE)

        # Draw the paddle and ball
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, RED, ball)
        
        # Draw the bricks
        for brick in bricks:
            pygame.draw.rect(screen, GREEN, brick)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

# Run the game
if __name__ == "__main__":
    main()