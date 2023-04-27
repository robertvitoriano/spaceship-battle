import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Scenes.menu_scene import MenuScene
from src.Scenes.first_scene import FirstScene

from src.game import Game

def main():
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

    menu_scene = MenuScene(background_image="assets/images/menu_test.png", background_music="assets/music/background.wav", screen=screen)
    first_scene = FirstScene(background_image="assets/images/background.png", background_music="assets/music/background.wav", screen=screen, player= player, enemy=enemy)
    scenes = [menu_scene, first_scene]
    game = Game(scenes=scenes, starting_scene=1)

    game.run()



if __name__ == '__main__':
    main()
