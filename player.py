
import pygame
from bullet import Bullet

class Player:
    def __init__(self, screen):

        # Get display info
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.speed = 0
        self.player_speed_rate = 8
        self.player_right_collision = False
        self.player_left_collision = False
        self.image = pygame.image.load('./player.png')
        self.x_coordinate = self.screen_width/2 - self.image.get_width()
        self.x_position = self.x_coordinate
        self.y_position = self.screen_height - 100
        self.shot_sound = pygame.mixer.Sound('laser.wav')
        self.bullet_image = pygame.image.load('./bullet.png')
        self.bullet_speed = 5
        self.bullets = []
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x_position, self.y_position))

    def handle_wall_collisions(self):
        if self.x_position >= self.screen_width - self.image.get_width():
            self.player_right_collision = True
        else:
            self.player_right_collision = False

        if self.x_position <= 0:
            self.player_left_collision = True
        else:
            self.player_left_collision = False

    def handle_x_movements(self, keys):
        if keys[pygame.K_LEFT] and not self.player_left_collision:
            self.speed -= self.player_speed_rate

        if keys[pygame.K_RIGHT] and not self.player_right_collision:
            self.speed += self.player_speed_rate

        self.x_position = self.x_coordinate + self.speed

    def handle_shot(self, keys):
        if keys[pygame.K_SPACE]:
            self.shot_sound.play()
            bullet_y_position = self.y_position
            bullet_x_position = self.x_position + self.image.get_width() / 2 - self.bullet_image.get_width() / 2
            bullet = Bullet(bullet_x_position, bullet_y_position)
            self.bullets.append(bullet)

    def handle_bullets(self):
        new_bullets = []

        for bullet in self.bullets:
            bullet.update()
            if bullet.y_position > 0:
                self.screen.blit(self.bullet_image, (bullet.x_position, bullet.y_position))
                new_bullets.append(bullet)
            else:
                del bullet

        self.bullets = new_bullets
