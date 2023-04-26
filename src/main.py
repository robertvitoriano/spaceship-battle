import pygame
from src.game import Game
from src.Scenes.menu_scene import MenuScene
from src.Scenes.first_scene import FirstScene
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

observer = Observer()
observer.schedule(MyHandler(), path='.')
observer.start()

pygame.init()
pygame.mixer.init()

WIDTH=800
HEIGHT=600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Space Invaders")

player = Player(screen,
                'assets/images/player.png',
                'assets/music/laser.wav',
                'assets/images/bullet.png')
enemy = Enemy(screen,
            'assets/images/enemy.png',
            'assets/music/laser.wav',
            'assets/images/bullet.png')

menu_scene = MenuScene()
first_scene = FirstScene(background_image="assets/images/background.png", player= player, enemy=enemy)
scenes = [menu_scene, first_scene]
game = Game(scenes=scenes, starting_scene=0)

game.start()
