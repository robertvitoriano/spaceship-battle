from src.Entities.spaceship import Spaceship
import pygame
import random
class Enemy(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, id,lives = 2, dificult_y_rate = 2, speed_rate=5):
        super().__init__(screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, lives = lives, speed_rate=speed_rate)

        self.x_position = random.randint(0, self.screen_width - self.image.get_width())
        self.id = id
        self.y_position = 0
        self.direction = 1
        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())
        self.speed_rate_y = 5 * dificult_y_rate
        self.is_out_screen = False
        self.point_to_get_down = random.randint(0, self.image.get_width())


    def handle_wall_collisions(self):
        if self.x_position <= 0 or self.x_position >= self.screen_width - self.image.get_width():
            self.direction = self.direction * -1
            self.y_position += self.speed_rate_y

    def handle_shot(self, keys=None):

        pass

    def draw_fires(self):
        pass

    def handle_x_movements(self, keys=None):
        self.x_position += self.speed_rate * self.direction

        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())

        self.handle_gone_out_screen()


    def handle_gone_out_screen(self):
        if self.y_position >= self.screen.get_height():
            self.is_out_screen = True

    def is_enemy_out_screen(self):
        return self.is_out_screen

    def get_enemy_id(self):
        return self.id

    def handle_hit(self):
        is_not_being_hit = self.hit_timer is None and self.image == self.original_image
        if is_not_being_hit :
            self.change_to_hit_image()






