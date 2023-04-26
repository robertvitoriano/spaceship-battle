import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.bullet import Bullet
class Game:
    def __init__(scenes, starting_scene, screen):

        self.__scenes = scenes
        self.__current_scene = starting_scene
        self.__running = True

    @staticmethod
    def change_scene(new_scene_number):
        self.__current_scene = new_scene_number

    def start():
        background_music_volume = 0
        background_music = pygame.mixer.Sound('assets/music/background.wav')
        background_music.set_volume(background_music_volume)
        background_music.play(-1)

        # create the screen
        background_image = pygame.image.load("assets/images/background.png")

        while self.__running:
            scenes[current_scene].draw()
            keys = pygame.key.get_pressed()

            scenes[current_scene].player.handle_x_movements(keys)
            scenes[current_scene].player.handle_wall_collisions()
            scenes[current_scene].player.handle_shot(keys)
            scenes[current_scene].player.handle_bullets()
            scenes[current_scene].enemy.handle_x_movements(keys)
            scenes[current_scene].enemy.handle_wall_collisions()

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        pygame.quit()


