import pygame
from src.Entities.bullet import Bullet
from src.Entities.spaceship import Spaceship
from src.Entities.directions_enum import DirectionsEnum
class Player(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, bullet_image_path, bullet_volume):

        super().__init__(screen, image_path, shot_sound_path, bullet_image_path, bullet_volume)

        self.x_position = self.screen_width/2 - self.image.get_width()
        self.y_position = self.screen_height - 100

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
            bullet_y_position = self.y_position
            bullet_x_position = self.x_position + self.image.get_width() / 2 - self.bullet_image.get_width() / 2
            bullet = Bullet(x=bullet_x_position, y=bullet_y_position,direction=DirectionsEnum.DOWN.value)
            self.bullets.append(bullet)

    def draw_bullets(self):
        new_bullets = []

        for bullet in self.bullets:
            bullet.update()
            if bullet.y_position > 0:
                self.screen.blit(self.bullet_image,
                                    (bullet.x_position, bullet.y_position))
                new_bullets.append(bullet)
            else:
                del bullet

        self.bullets = new_bullets
