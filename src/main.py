import pygame
from enum import Enum
from src.game import Game
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Scenes.menu_scene import MenuScene
from src.Scenes.first_scene import FirstScene
from src.Scenes.scenes_enum import ScenesEnum


def main():
    WIDTH=800
    HEIGHT=600

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Space Invaders")

    player = Player(screen,
                    'assets/images/player.png',
                    'assets/music/laser.wav',
                    'assets/images/player_laser.png', 0.1)
    enemy = Enemy(screen,
                'assets/images/enemy.png',
                'assets/music/laser.wav',
                'assets/images/bullet.png',
                0.1
                )

    scenes = {
        ScenesEnum.MENU_SCENE: MenuScene(background_image="assets/images/menu_background.png", background_music="assets/music/menu_music.mp3", screen=screen, ),
        ScenesEnum.FIRST_SCENE: FirstScene(background_image="assets/images/background.png", background_music="assets/music/background.wav", screen=screen, player= player, enemy=enemy)
    }
    game = Game.get_instance(scenes, ScenesEnum.MENU_SCENE)

    game.run()

if __name__ == '__main__':
    main()
