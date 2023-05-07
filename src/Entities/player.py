import pygame
from src.Entities.fire import Fire
from src.Entities.spaceship import Spaceship
from src.Entities.directions_enum import DirectionsEnum
from src.utils.constants import PLAYER_SPEED, LIFE_SIZE,LIFE_X_POSITION,LIFE_MARGIN,PLAYER_Y_OFFSET_INITIAL_POSITION, FIRE_VOLUME_MULTPLIER, LIFE_Y_POSITION

class Player(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, life_image_path, lives, hit_sound_path = None):

        super().__init__(screen, image_path, shot_sound_path, fire_image_path,hit_image_path, fire_volume, lives=lives, hit_sound_path=hit_sound_path)

        self.x_position = screen.get_width()/2 - self.image.get_width()/2
        self.y_position = self.screen_height - PLAYER_Y_OFFSET_INITIAL_POSITION
        self.fires = []
        self.life_y_position = LIFE_Y_POSITION
        self.life_image = pygame.image.load(life_image_path)
        self.life = pygame.transform.scale(self.life_image, (LIFE_SIZE,LIFE_SIZE))
        self.life_x_position = LIFE_X_POSITION
        self.life_margin = LIFE_MARGIN
        self.life_distance = self.life.get_width() + self.life_margin
        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())
        self.has_shot = False
        self.speed_rate = PLAYER_SPEED
        self.max_y_position = screen.get_height()/2
        self.down_collision = False
        self.limit_y_collision = False

    def handle_wall_collisions(self):
        if self.x_position >= self.screen_width - self.image.get_width():
            self.right_collision = True
        else:
            self.right_collision = False

        if self.x_position <= 0:
            self.left_collision = True
        else:
            self.left_collision = False

        if self.y_position >= self.screen.get_height() - self.get_height()*2:
            self.down_collision = True
        else:
            self.down_collision = False


        if self.y_position <= self.max_y_position:
            self.limit_y_collision = True
        else:
            self.limit_y_collision = False

    def handle_x_movements(self, keys):
        if keys[pygame.K_LEFT] and not self.left_collision:
            self.x_position -= self.speed_rate

        if keys[pygame.K_RIGHT] and not self.right_collision:
            self.x_position += self.speed_rate

    def handle_y_movements(self, keys):
        if keys[pygame.K_UP] and not self.limit_y_collision:
            self.y_position -= self.speed_rate

        if keys[pygame.K_DOWN] and not self.down_collision:
            self.y_position += self.speed_rate

        self.rect.top = self.y_position
    def get_hit_volume(self):
        return self.fire_volume*FIRE_VOLUME_MULTPLIER

    def handle_shot(self, keys):
        if keys[pygame.K_SPACE] and not self.has_shot:
            self.has_shot = True
            self.shot_sound.play()
            fire_y_position = self.y_position
            fire_x_position = self.x_position + self.image.get_width() / 2 - self.fire_image.get_width() / 2
            fire = Fire(x=fire_x_position, y=fire_y_position,direction=DirectionsEnum.DOWN.value, fire_image= self.fire_image, screen=self.screen, hit_volume=self.get_hit_volume())
            self.fires.append(fire)
        elif not keys[pygame.K_SPACE]:
            self.has_shot =  False

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
        if(fire_index< len(self.fires)):
         del self.fires[fire_index]

    def draw_lives(self):
        for i in range(self.remaining_lives):
            life_x_position = self.life_x_position + (self.life_distance * i)
            self.screen.blit(self.life, (life_x_position, self.life_y_position))

    def get_rect(self):
        return self.rect






