from src.Entities.spaceship import Spaceship
import pygame

class Enemy(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, bullet_image_path, bullet_volume):
        super().__init__(screen, image_path, shot_sound_path, bullet_image_path, bullet_volume)

        self.x_position = self.screen_width / 2 - self.image.get_width()
        self.y_position = 100
        self.direction = 1

    def handle_wall_collisions(self):
        if self.x_position <= 0 or self.x_position >= self.screen_width - self.image.get_width():
            self.direction = self.direction * -1

    def handle_shot(self, keys=None):
        pass

    def draw_bullets(self):
        pass

    def handle_x_movements(self, keys=None):
        self.speed += self.speed_rate * self.direction
        self.x_position = self.speed
