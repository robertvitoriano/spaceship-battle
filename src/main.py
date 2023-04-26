import pygame
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer

from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.bullet import Bullet
from src.watcher import Watcher

observer = Observer()
observer.schedule(Watcher(), path='./src')
observer.start()
# Initialize the Pygame
pygame.init()
pygame.mixer.init()


# GAME SETTINGS
WIDTH = 800
HEIGHT = 600
running = True
background_music_volume = 0.1
background_music = pygame.mixer.Sound('assets/music/background.wav')
background_music.set_volume(background_music_volume)
background_music.play(-1)
scenes = []

# create the screen
pygame.display.set_caption("Space Invaders")
background_image = pygame.image.load("assets/images/background.png")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Player(screen,
                'assets/images/player.png',
                'assets/music/laser.wav',
                'assets/images/bullet.png')
enemy = Enemy(screen,
              'assets/images/enemy.png',
              'assets/music/laser.wav',
              'assets/images/bullet.png')

while running:
    screen.blit(background_image, (0, 0))
    keys = pygame.key.get_pressed()

    player.handle_x_movements(keys)
    player.handle_wall_collisions()
    player.handle_shot(keys)
    player.handle_bullets()

    enemy.handle_x_movements(keys)
    enemy.handle_wall_collisions()

    player.draw()
    enemy.draw()

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
