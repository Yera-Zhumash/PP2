import pygame
import sys
from pygame import mixer

pygame.init()
mixer.init()

# Список 
music_files = ["song1.mp3", "song2.mp3", "song3.mp3"]
current_track = 0

# 1тр
mixer.music.load(music_files[current_track])

#  окна
screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

running = True
while running:
    screen.fill((200, 200, 200))  #  фон
    pygame.display.flip()  # Обновляем 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Play
                mixer.music.play()
                print("Playing:", music_files[current_track])
            elif event.key == pygame.K_s:  # Stop
                mixer.music.stop()
                print("Music Stopped")
            elif event.key == pygame.K_n:  # Next track
                current_track = (current_track + 1) % len(music_files)
                mixer.music.load(music_files[current_track])
                mixer.music.play()
                print("Next track:", music_files[current_track])
            elif event.key == pygame.K_b:  # Previous track
                current_track = (current_track - 1) % len(music_files)
                mixer.music.load(music_files[current_track])
                mixer.music.play()
                print("Previous track:", music_files[current_track])

pygame.quit()
sys.exit()
