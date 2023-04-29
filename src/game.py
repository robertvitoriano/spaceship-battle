import pygame
import time

from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.fire import Fire
from src.Scenes.scenes_enum import ScenesEnum

game = None

class Game:
    def __init__(self, scenes, starting_scene, main_volume):
        pygame.init()
        pygame.mixer.init()

        self.scenes = scenes
        self.current_scene = starting_scene
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.width, self.height = 800, 600
        self.main_volume = main_volume

    @classmethod
    def get_instance(cls, scenes=None, starting_scene = 0, main_volume = 0.4):
        global game
        if game is None and scenes is not None:
            game = Game(scenes=scenes, starting_scene=starting_scene, main_volume=main_volume)
        return game

    def change_scene(self, new_scene_number):
        self.scenes[self.current_scene].stop_background_music()
        self.current_scene = new_scene_number
        self.scenes[self.current_scene].play_background_music(self.main_volume)

    def update(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        self.scenes[self.current_scene].handle_scene_events(events,keys)
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_game()

    def draw(self):
        self.scenes[self.current_scene].draw()

        pygame.display.update()

    def stop(self):
        self.running = False

    def quit_game(self):
        self.stop()

    def run(self):
        self.scenes[self.current_scene].play_background_music(self.main_volume)

        while self.running:
            self.draw()
            self.update()

            self.clock.tick(self.FPS)

        # shut down all Pygame modules
        pygame.quit()
