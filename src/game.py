import pygame
import time

from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.fire import Fire

game = None

class Game:
    def __init__(self, scenes, starting_scene):
        pygame.init()
        pygame.mixer.init()

        self.scenes = scenes
        self.current_scene = starting_scene
        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.width, self.height = 800, 600

    @classmethod
    def get_instance(cls, scenes=None, starting_scene = 0):
        global game
        if game is None and scenes is not None:
            game = Game(scenes, starting_scene)
        return game

    def change_scene(self, new_scene_number):
        self.scenes[self.current_scene].stop_background_music()
        self.current_scene = new_scene_number
        self.scenes[self.current_scene].play_background_music(0.1)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            self.scenes[self.current_scene].handle_scene_events(event)

    def handle_enemy_hit(self):
        fires = self.scenes[self.current_scene].player.get_fires()
        enemy_group = pygame.sprite.Group()
        enemy_group.add(self.scenes[self.current_scene].enemy)
        for i, fire in  enumerate(fires):
            collision = pygame.sprite.spritecollide(fire, enemy_group, True)

            if collision:
                fire.play_hit_sound()
                del self.scenes[self.current_scene].enemy
                self.scenes[self.current_scene].player.remove_fire(i)

    def update(self):

        keys = pygame.key.get_pressed()
        if self.scenes[self.current_scene].player is not None:
            self.scenes[self.current_scene].player.handle_x_movements(keys)
            self.scenes[self.current_scene].player.handle_wall_collisions()
            self.scenes[self.current_scene].player.handle_shot(keys)
        if hasattr(self.scenes[self.current_scene], 'enemy') and self.scenes[self.current_scene].enemy is not None:
            self.scenes[self.current_scene].enemy.handle_x_movements(keys)
            self.scenes[self.current_scene].enemy.handle_wall_collisions()
            self.handle_enemy_hit()

    def draw(self):
        self.scenes[self.current_scene].draw()
        if self.scenes[self.current_scene].player is not None:
            self.scenes[self.current_scene].player.draw_fires()

        # update display
        pygame.display.update()

    def stop(self):
        self.running = False

    def quit_game(self):
        self.stop()
        pygame.quit()

    def run(self):
        self.scenes[self.current_scene].play_background_music(0.1)

        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(self.FPS)

        # shut down all Pygame modules
        pygame.quit()
