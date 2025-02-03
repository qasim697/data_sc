import pygame
import random
import time

# Initialize pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Set display dimensions
dis_width = 800
dis_height = 600

# Create the display
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Car Racing Game')

# Set clock for controlling the game speed
clock = pygame.time.Clock()

# Load car images
car_width = 60
car_height = 100
player_car_img = pygame.image.load('player_car.png')  # Replace with your player car image
enemy_car_img = pygame.image.load('enemy_car.png')    # Replace with your enemy car image

# Resize car images
player_car_img = pygame.transform.scale(player_car_img, (car_width, car_height))
enemy_car_img = pygame.transform.scale(enemy_car_img, (car_width, car_height))

# Function to display the player's score
def display_score(score):
    font = pygame.font.SysFont(None, 35)
    text = font.render("Score: " + str(score), True, black)
    dis.blit(text, [10, 10])

# Function to draw enemy cars
def draw_enemy_car(x, y):
    dis.blit(enemy_car_img, (x, y))

# Function to draw the player's car
def draw_player_car(x, y):
    dis.blit(player_car_img, (x, y))

# Function to display a message on the screen
def message(msg, color):
    font = pygame.font.SysFont(None, 50)
    text = font.render(msg, True, color)
    dis.blit(text, [dis_width / 6, dis_height / 3])

# Main game loop
def gameLoop():
    game_over = False
    game_close = False

    # Initial position of the player's car
    player_x = dis_width * 0.45
    player_y = dis_height * 0.8

    # Change in position
    player_x_change = 0

    # Enemy car properties
    enemy_x = random.randrange(0, dis_width - car_width)
    enemy_y = -600
    enemy_speed = 5

    # Score
    score = 0

    while not game_over:

        while game_close:
            dis.fill(white)
            message("You Crashed! Press Q-Quit or C-Play Again", red)
            display_score(score)
            pygame.display.update()

            # Check for player input after game over
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_c:
                        gameLoop()

        # Handle keyboard events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player_x_change = -5
                elif event.key == pygame.K_RIGHT:
                    player_x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    player_x_change = 0

        # Update player's car position
        player_x += player_x_change

        # Prevent the car from going out of bounds
        if player_x < 0:
            player_x = 0
        elif player_x > dis_width - car_width:
            player_x = dis_width - car_width

        # Move the enemy car
        enemy_y += enemy_speed

        # Draw the background
        dis.fill(white)

        # Draw the player's car
        draw_player_car(player_x, player_y)

        # Draw the enemy car
        draw_enemy_car(enemy_x, enemy_y)

        # Check for collision
        if player_y < enemy_y + car_height and player_y + car_height > enemy_y:
            if player_x < enemy_x + car_width and player_x + car_width > enemy_x:
                game_close = True

        # Reset enemy car position and increase score
        if enemy_y > dis_height:
            enemy_y = -car_height
            enemy_x = random.randrange(0, dis_width - car_width)
            score += 1
            enemy_speed += 0.5  # Increase difficulty

        # Display the score
        display_score(score)

        # Update the display
        pygame.display.update()

        # Control game speed
        clock.tick(60)

    # Quit pygame
    pygame.quit()
    quit()

# Start the game
gameLoop()