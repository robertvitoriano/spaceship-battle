from src.Entities.spaceship import Spaceship
from src.utils.constants import DEBUG_MODE
from src.Entities.directions_enum import DirectionsEnum
from src.Entities.fire import Fire

import pygame
import random
class Enemy(Spaceship):
    def __init__(self,
                 screen,
                 image_path,
                 shot_sound_path,
                 fire_image_path,
                 hit_image_path,
                 fire_volume,
                 id,
                 x_position,
                 y_position,
                 lives = 2,
                 speed_rate=5,
                 explosion_sprites = []):
        super().__init__(screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, lives = lives, speed_rate=speed_rate)
        self.x_position = x_position
        self.y_position = y_position
        self.id = id
        self.direction = 1
        self.time_to_get_out_of_hit_state = 400
        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())
        self.speed_rate_y = 50
        self.is_out_screen = False
        self.point_to_get_down = random.randint(0, self.image.get_width())
        self.should_remove = False
        self.explosion_sprites=explosion_sprites
        self.sprite_counter = 0
        self.current_explosion_sprite_index = 1
        self.coordinates_font = pygame.font.SysFont(None, 35)
        self.debug = DEBUG_MODE
        self.fires = []

    def handle_wall_collisions(self):

        if self.image is not None:
            if self.x_position <= 0 or self.x_position >= self.screen_width - self.image.get_width():
                self.direction = self.direction * -1
                self.y_position += self.speed_rate_y if self.y_position > self.get_height() else self.speed_rate *4

    def handle_shot(self, keys=None):

        pass

    def draw_fires(self):
        pass

    def handle_x_movements(self, keys=None):
        is_not_being_hit = self.hit_timer is None and self.image == self.original_image
        if is_not_being_hit:
            self.x_position += (self.speed_rate * self.direction)
            self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())

        self.get_out_of_screen()


    def get_out_of_screen(self):
        if self.y_position >= self.screen.get_height():
            self.is_out_screen = True

    def is_enemy_out_screen(self):
        return self.is_out_screen

    def get_enemy_id(self):
        return self.id

    def handle_hit(self):
        is_not_being_hit = self.hit_timer is None and self.image == self.original_image
        if is_not_being_hit :
            self.set_hit_timer()
            self.draw_explosion_animation()


    def verify_hit_state(self):
        if self.hit_timer is not None and pygame.time.get_ticks() >= self.hit_timer:
            self.hit_timer = None
            self.should_remove = True

    def draw_coordinates(self):
        if self.image is not None and self.debug:
            coordinates_surface = self.coordinates_font.render("X: "+str(self.x_position)+"," +"Y "+ str(self.y_position), True, (255, 0, 0))
            coordinates_rect = coordinates_surface.get_rect()
            coordinates_rect.center = (self.x_position+20, self.y_position )
            self.screen.blit(coordinates_surface, coordinates_rect)

    def draw_explosion_animation(self):
        if(len(self.explosion_sprites) > 0):
            time_per_explosion_sprite =int(self.time_to_get_out_of_hit_state/len(self.explosion_sprites))

            current_explosion_sprite = self.explosion_sprites[self.current_explosion_sprite_index-1]
            if(pygame.time.get_ticks() == self.sprite_counter):
                self.current_explosion_sprite_index+=1
                self.sprite_counter = pygame.time.get_ticks() + time_per_explosion_sprite

            self.image = None
            self.screen.blit(current_explosion_sprite, self.rect.copy())
            pygame.display.update()


            self.sprite_counter = pygame.time.get_ticks()

    def draw(self):
        super().draw()
        self.draw_coordinates()
        self.draw_fires()


    def should_remove_enemy(self):
        return self.should_remove


    def handle_shot(self):
        if self.image is not None and len(self.fires) == 0:
            self.shot_sound.play()
            fire_y_position = self.y_position
            fire_x_position = self.x_position + self.image.get_width() / 2 - self.fire_image.get_width() / 2
            fire = Fire(x=fire_x_position, y=fire_y_position,direction=DirectionsEnum.DOWN.value, fire_image= self.fire_image, screen=self.screen, hit_volume=self.get_hit_volume(), speed=25)
            self.fires.append(fire)

    def draw_fires(self):
        if len(self.fires) == 0: return

        self.fires[0].update()
        if self.fires[0].y_position < self.screen.get_height():
            self.fires[0].draw(self.fires[0].x_position, self.fires[0].y_position)
        else:
            self.fires = []

    def get_fires(self):
        return self.fires

    def is_above(self):
       return  self.y_position < self.height


