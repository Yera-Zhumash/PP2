import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Racer Game")

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Clock for controlling frame rate
clock = pygame.time.Clock()

# Load images
player_img = pygame.image.load("Player.png")  # Player car
coin_img = pygame.image.load("Coin.png")
coin_img = pygame.transform.scale(coin_img, (30, 30))  # Resize coin
enemy_img = pygame.image.load("Enemy.png")  # Enemy car

# Load sounds
crash_sound = pygame.mixer.Sound("crash.wav")

# Player properties
player_width = 50
player_height = 100
player_x = (SCREEN_WIDTH // 2) - (player_width // 2)
player_y = SCREEN_HEIGHT - player_height - 20
player_speed = 5

# Coin properties
coin_width = 30
coin_height = 30
coin_x = random.randint(40, SCREEN_WIDTH - 40)
coin_y = -coin_height
coin_speed = 3
coin_collected = 0
coin_weight = random.randint(1, 3)  # Random weight for the coin

# Enemy properties
enemy_speed = 5
enemy_x = random.randint(40, SCREEN_WIDTH - 40)
enemy_y = -player_height

# Speed increase threshold
N = 5  # Speed increases every N coins collected

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Function to display coins collected
def show_coins(coins):
    text = font_small.render(f"Coins: {coins}", True, YELLOW)
    screen.blit(text, (10, 40))

# Function to display game over screen
def show_game_over():
    screen.fill(RED)
    screen.blit(game_over, (30, 250))
    pygame.display.update()
    time.sleep(2)
    pygame.quit()
    exit()

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < SCREEN_WIDTH - player_width:
        player_x += player_speed

    # Move coin
    coin_y += coin_speed
    if coin_y > SCREEN_HEIGHT:
        coin_x = random.randint(40, SCREEN_WIDTH - 40)
        coin_y = -coin_height
        coin_weight = random.randint(1, 3)  # Assign a new random weight

    # Move enemy
    enemy_y += enemy_speed
    if enemy_y > SCREEN_HEIGHT:
        enemy_x = random.randint(40, SCREEN_WIDTH - 40)
        enemy_y = -player_height

    # Check for collision with coin
    if (player_x < coin_x + coin_width and player_x + player_width > coin_x and
            player_y < coin_y + coin_height and player_y + player_height > coin_y):
        coin_collected += coin_weight  # Increase score by coin weight
        coin_x = random.randint(40, SCREEN_WIDTH - 40)
        coin_y = -coin_height
        coin_weight = random.randint(1, 3)  # Assign a new random weight

        # Increase enemy speed after collecting N coins
        if coin_collected % N == 0:
            enemy_speed += 1

    # Check for collision with enemy
    if (player_x < enemy_x + player_width and player_x + player_width > enemy_x and
            player_y < enemy_y + player_height and player_y + player_height > enemy_y):
        pygame.mixer.Sound.play(crash_sound)
        time.sleep(1)
        show_game_over()

    # Draw background
    screen.blit(background, (0, 0))
    screen.blit(player_img, (player_x, player_y))
    screen.blit(coin_img, (coin_x, coin_y))
    screen.blit(enemy_img, (enemy_x, enemy_y))  # Draw enemy car
    show_coins(coin_collected)

    # Update display
    pygame.display.update()
    clock.tick(60)

# Quit Pygame
pygame.quit()
