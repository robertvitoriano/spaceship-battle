import pygame
from src.Entities.fire import Fire
from src.Entities.spaceship import Spaceship
from src.Entities.directions_enum import DirectionsEnum
class Player(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, fire_volume):

        super().__init__(screen, image_path, shot_sound_path, fire_image_path, fire_volume)

        self.x_position = self.screen_width/2 - self.image.get_width()
        self.y_position = self.screen_height - 100
        self.fires = []

    def handle_wall_collisions(self):
        if self.x_position >= self.screen_width - self.image.get_width():
            self.right_collision = True
        else:
            self.right_collision = False

        if self.x_position <= 0:
            self.left_collision = True
        else:
            self.left_collision = False

    def handle_x_movements(self, keys):
        if keys[pygame.K_LEFT] and not self.left_collision:
            self.speed -= self.speed_rate

        if keys[pygame.K_RIGHT] and not self.right_collision:
            self.speed += self.speed_rate

        self.x_position =  self.speed

    def handle_shot(self, keys):
        if keys[pygame.K_SPACE]:
            self.shot_sound.play()
            fire_y_position = self.y_position
            fire_x_position = self.x_position + self.image.get_width() / 2 - self.fire_image.get_width() / 2
            fire = Fire(x=fire_x_position, y=fire_y_position,direction=DirectionsEnum.DOWN.value, fire_image= self.fire_image, screen=self.screen)
            self.fires.append(fire)

    def draw_fires(self):
        new_fires = []

        for fire in self.fires:
            fire.update()
            if fire.y_position > 0:
                fire.draw(fire.x_position, fire.y_position)
                new_fires.append(fire)
            else:
                del fire

        self.fires = new_fires



    def get_fires(self):
        return self.fires

    def remove_fire(self,fire_index):
        del self.fires[fire_index]
