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
    main_volume = 0.3

    player = Player(screen,
                    image_path='assets/images/player.png',
                    shot_sound_path='assets/music/laser.wav',
                    fire_image_path='assets/images/player_laser.png',
                    hit_image_path='assets/images/player_hit.png',
                    live_image_path='assets/images/heart_image.png',
                    fire_volume=0.1,
                    lives_count=5)


    scenes = {
        ScenesEnum.MENU_SCENE: MenuScene(background_image="assets/images/menu_background.jpg",
                                         background_music="assets/music/menu_music.mp3",
                                         screen=screen,background_music_volume=main_volume,
                                         background_speed=15),

        ScenesEnum.FIRST_SCENE: FirstScene(background_image="assets/images/background.png",
                                           background_music="assets/music/start.wav",
                                           screen=screen, player= player,
                                           background_music_volume=main_volume,
                                           background_speed=20)
    }
    game = Game.get_instance(scenes=scenes, starting_scene=ScenesEnum.MENU_SCENE, main_volume=main_volume)

    game.run()

if __name__ == '__main__':
    main()
