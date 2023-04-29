from src.Entities.spaceship import Spaceship
import pygame
import random
class Enemy(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, id,life = 10):
        super().__init__(screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume)

        self.x_position =  random.randint(0, self.screen_width - self.image.get_width())
        self.id = id
        self.y_position = 100
        self.direction = 1
        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())
        self.life = life


    def handle_wall_collisions(self):
        if self.x_position <= 0 or self.x_position >= self.screen_width - self.image.get_width():
            self.direction = self.direction * -1

    def handle_shot(self, keys=None):

        pass

    def draw_fires(self):
        pass

    def handle_x_movements(self, keys=None):
        self.x_position += self.speed_rate * self.direction

        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())



