import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.bullet import Bullet

class Game:
    def __init__(self, scenes, starting_scene):
        pygame.init()
        pygame.mixer.init()

        self.__scenes = scenes
        self.__current_scene = starting_scene
        self.__running = True
        self.running = False
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.width, self.height = 800, 600


    @staticmethod
    def change_scene(new_scene_number):
        self.__current_scene = new_scene_number
        self.__scenes[self.__current_scene].play_background_music(0.5)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        self.__scenes[self.__current_scene].player.handle_x_movements(keys)
        self.__scenes[self.__current_scene].player.handle_wall_collisions()
        self.__scenes[self.__current_scene].player.handle_shot(keys)
        self.__scenes[self.__current_scene].enemy.handle_x_movements(keys)
        self.__scenes[self.__current_scene].enemy.handle_wall_collisions()

    def draw(self):
        self.__scenes[self.__current_scene].draw()
        self.__scenes[self.__current_scene].player.draw_bullets()

        # update display
        pygame.display.update()

    def stop(self):
        self.running = False

    def run(self):
        self.__scenes[self.__current_scene].play_background_music(0.5)
        while self.__running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(self.FPS)

        # shut down all Pygame modules
        pygame.quit()
