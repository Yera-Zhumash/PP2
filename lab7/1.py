import pygame
import sys
import math
import time

pygame.init()

WIDTH, HEIGHT = 500, 500
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")

clock_img = pygame.image.load("mickeyclock.jpeg")
clock_img = pygame.transform.scale(clock_img, (WIDTH, HEIGHT))
clock_rect = clock_img.get_rect(center=(WIDTH//2, HEIGHT//2))

hand_img = pygame.Surface((200, 10), pygame.SRCALPHA)
pygame.draw.rect(hand_img, (0, 0, 0), (0, 0, 200, 10))

clock = pygame.time.Clock()
running = True

while running:
    screen.fill((255, 255, 255))
    screen.blit(clock_img, clock_rect)

    current_time = time.localtime()
    sec_angle = -current_time.tm_sec * 6
    min_angle = -current_time.tm_min * 6
    
    min_hand = pygame.transform.rotate(hand_img, min_angle)
    sec_hand = pygame.transform.rotate(hand_img, sec_angle)
    
    min_rect = min_hand.get_rect(center=clock_rect.center)
    sec_rect = sec_hand.get_rect(center=clock_rect.center)
    
    screen.blit(min_hand, min_rect)
    screen.blit(sec_hand, sec_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()
