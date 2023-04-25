import pygame
from player import Player
from bullet import Bullet
# Initialize the Pygame
pygame.init()
pygame.mixer.init()

# GAME SETTINGS
WIDTH = 800
HEIGHT = 600
running = True
background_music_volume = 0.3
background_music = pygame.mixer.Sound('background.wav')
background_music.set_volume(background_music_volume)
background_music.play(-1)

# create the screen
pygame.display.set_caption("Space Invaders")
background_image = pygame.image.load("background.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player(screen)

while running:
    screen.blit(background_image, (0, 0))
    keys = pygame.key.get_pressed()

    player.handle_x_movements(keys)
    player.handle_wall_collisions()
    player.handle_shot(keys)
    player.handle_bullets()

    player.draw()
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
