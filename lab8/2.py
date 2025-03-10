import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
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

# Score and level
score = 0
level = 1

# Font for displaying score and level
font = pygame.font.SysFont(None, 35)

# Function to display score and level
def show_score_level(score, level):
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

# Function to draw the snake
def draw_snake(snake_block, snake_list):
    for block in snake_list:
        pygame.draw.rect(screen, GREEN, [block[0], block[1], snake_block, snake_block])

# Function to generate food at a random position
def generate_food(snake_list):
    while True:
        food_x = round(random.randrange(0, SCREEN_WIDTH - snake_block) / 20.0) * 20.0
        food_y = round(random.randrange(0, SCREEN_HEIGHT - snake_block) / 20.0) * 20.0
        if [food_x, food_y] not in snake_list:  # Ensure food doesn't spawn on the snake
            return food_x, food_y

# Game loop
running = True
snake_x = SCREEN_WIDTH / 2
snake_y = SCREEN_HEIGHT / 2
snake_x_change = 0
snake_y_change = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_x_change = -snake_block
                snake_y_change = 0
            elif event.key == pygame.K_RIGHT:
                snake_x_change = snake_block
                snake_y_change = 0
            elif event.key == pygame.K_UP:
                snake_y_change = -snake_block
                snake_x_change = 0
            elif event.key == pygame.K_DOWN:
                snake_y_change = snake_block
                snake_x_change = 0

    # Check for border collision
    if snake_x >= SCREEN_WIDTH or snake_x < 0 or snake_y >= SCREEN_HEIGHT or snake_y < 0:
        running = False

    # Update snake position
    snake_x += snake_x_change
    snake_y += snake_y_change
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, [food_x, food_y, snake_block, snake_block])
    snake_head = [snake_x, snake_y]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    # Check for self-collision
    for block in snake_list[:-1]:
        if block == snake_head:
            running = False

    # Draw snake and food
    draw_snake(snake_block, snake_list)
    show_score_level(score, level)
    pygame.display.update()

    # Check for food collision
    if snake_x == food_x and snake_y == food_y:
        food_x, food_y = generate_food(snake_list)
        snake_length += 1
        score += 1

        # Increase level and speed
        if score % 3 == 0:  # Increase level every 3 foods
            level += 1
            snake_speed += 5  # Increase speed

    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()