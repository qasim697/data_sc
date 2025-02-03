import pygame
import random

# Initialize Pygame
pygame.init()

# Game Window Dimensions
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Birds in the Forest')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BROWN = (139, 69, 19)
BLUE = (0, 191, 255)

# Frame Rate
FPS = 60
clock = pygame.time.Clock()

# Bird Properties
bird_width = 40
bird_height = 40
bird_x = 100
bird_y = HEIGHT // 2
bird_velocity = 0
gravity = 0.5
jump_strength = -10

# Load bird image
bird_img = pygame.Surface((bird_width, bird_height))
bird_img.fill((255, 255, 0))  # Representing the bird with a yellow square for now.

# Forest Background (simple)
forest_background = pygame.Surface((WIDTH, HEIGHT))
forest_background.fill((34, 139, 34))  # A simple forest green background for now

# Obstacle (tree) Properties
tree_width = 50
tree_height = random.randint(150, 450)
tree_x = WIDTH
tree_gap = 200  # Gap between trees
tree_velocity = 5

# Game Over Flag
game_over = False

# Fonts
font = pygame.font.SysFont('Arial', 30)

def draw_bird(x, y):
    window.blit(bird_img, (x, y))

def draw_trees(x, height):
    tree_surface = pygame.Surface((tree_width, height))
    tree_surface.fill(BROWN)
    window.blit(tree_surface, (x, HEIGHT - height))

def display_message(text, x, y):
    message = font.render(text, True, (255, 255, 255))
    window.blit(message, (x, y))

def game_loop():
    global bird_y, bird_velocity, game_over, tree_x, tree_height

    # Reset bird's position and velocity
    bird_y = HEIGHT // 2
    bird_velocity = 0
    tree_x = WIDTH
    game_over = False

    while not game_over:
        window.fill(WHITE)
        window.blit(forest_background, (0, 0))  # Draw the forest background

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:  # Bird jumps when space is pressed
                    bird_velocity = jump_strength

        # Bird movement (gravity and jump)
        bird_velocity += gravity
        bird_y += bird_velocity

        # Prevent bird from flying off the screen
        if bird_y <= 0:
            bird_y = 0
            bird_velocity = 0
        elif bird_y + bird_height >= HEIGHT:
            bird_y = HEIGHT - bird_height
            bird_velocity = 0

        # Draw the bird
        draw_bird(bird_x, bird_y)

        # Draw trees and move them to the left
        tree_x -= tree_velocity
        if tree_x + tree_width < 0:
            tree_x = WIDTH
            tree_height = random.randint(150, 450)

        draw_trees(tree_x, tree_height)

        # Check for collisions (simple collision detection with tree)
        if bird_x + bird_width > tree_x and bird_x < tree_x + tree_width:
            if bird_y + bird_height > HEIGHT - tree_height:
                display_message("GAME OVER", WIDTH // 3, HEIGHT // 3)
                game_over = True

        # Display score (simple score for each tree passed)
        display_message(f'Score: {int((WIDTH - tree_x) / 50)}', 10, 10)

        # Refresh the screen
        pygame.display.update()

        # Frame rate
        clock.tick(FPS)

# Start the game loop
game_loop()

# Quit Pygame
pygame.quit()
 