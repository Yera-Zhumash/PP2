import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Snake properties
snake_block = 20
snake_speed = 15
snake_list = []
snake_length = 1

# Food properties
food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0
food_weight = random.randint(1, 3)  # Random weight for the food
food_timer = time.time()  # Timer for food disappearance

# Function to generate food with a random weight
def generate_food():
    global food_x, food_y, food_weight, food_timer
    food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
    food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0
    food_weight = random.randint(1, 3)
    food_timer = time.time()  # Reset the timer

# Game loop
running = True
snake_x = SCREEN_WIDTH / 2
snake_y = SCREEN_HEIGHT / 2
snake_x_change = 0
snake_y_change = 0
last_direction = None  # To prevent changing direction twice

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and last_direction != "RIGHT":
                snake_x_change = -snake_block
                snake_y_change = 0
                last_direction = "LEFT"
            elif event.key == pygame.K_RIGHT and last_direction != "LEFT":
                snake_x_change = snake_block
                snake_y_change = 0
                last_direction = "RIGHT"
            elif event.key == pygame.K_UP and last_direction != "DOWN":
                snake_y_change = -snake_block
                snake_x_change = 0
                last_direction = "UP"
            elif event.key == pygame.K_DOWN and last_direction != "UP":
                snake_y_change = snake_block
                snake_x_change = 0
                last_direction = "DOWN"

    # Check if food has expired
    if time.time() - food_timer > 5:  # Food disappears after 5 seconds
        generate_food()

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change

    # Check for collision with borders
    if snake_x < 0 or snake_x >= SCREEN_WIDTH or snake_y < 0 or snake_y >= SCREEN_HEIGHT:
        running = False  # Game over if snake hits the border

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])

    # Draw snake
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

    # Check for collision with food
    if snake_x == food_x and snake_y == food_y:
        snake_length += food_weight  # Increase snake length by food weight
        generate_food()

    pygame.display.update()
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
