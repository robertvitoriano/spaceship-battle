import pygame
from src.Entities.fire import Fire
from src.Entities.spaceship import Spaceship
from src.Entities.directions_enum import DirectionsEnum
class Player(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, live_image_path, lives_count):

        super().__init__(screen, image_path, shot_sound_path, fire_image_path,hit_image_path, fire_volume)

        self.x_position = self.screen_width/2 - self.image.get_width()
        self.y_position = self.screen_height - 100
        self.fires = []
        self.lives_count = lives_count
        self.live_y_position = 100
        self.live_image = pygame.image.load(live_image_path)
        self.live = pygame.transform.scale(self.live_image, (64,64))
        self.live_x_position = 20
        self.live_margin = 15
        self.live_distance = self.live.get_width() + self.live_margin
        self.remaining_lives = lives_count

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

    def get_hit_volume(self):
        return self.fire_volume*4

    def handle_shot(self, keys):
        if keys[pygame.K_SPACE]:
            self.shot_sound.play()
            fire_y_position = self.y_position
            fire_x_position = self.x_position + self.image.get_width() / 2 - self.fire_image.get_width() / 2
            fire = Fire(x=fire_x_position, y=fire_y_position,direction=DirectionsEnum.DOWN.value, fire_image= self.fire_image, screen=self.screen, hit_volume=self.get_hit_volume())
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

    def draw_lives(self):
        for i in range(self.remaining_lives):
            live_x_position = self.live_x_position + (self.live_distance * i)
            self.screen.blit(self.live, (live_x_position, self.live_y_position))

    def decrease_lives(self):
        self.remaining_lives -=1




