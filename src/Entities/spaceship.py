import pygame
from abc import ABC, abstractmethod
from src.Scenes.scenes_enum import ScenesEnum

class Spaceship(pygame.sprite.Sprite, ABC):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, hit_image_path = None, fire_volume = 0.5, lives=5, speed_rate=8, hit_sound_path=None):
        super().__init__()
        pygame.mixer.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.speed = 0
        self.speed_rate = speed_rate
        self.right_collision = False
        self.left_collision = False
        self.image = pygame.image.load(image_path)
        self.original_image = self.image
        self.x_position = self.screen_width/2 - self.image.get_width()
        self.y_position = self.screen_height - 100
        self.shot_sound = pygame.mixer.Sound(shot_sound_path)
        self.fire_image = pygame.image.load(fire_image_path)
        self.hit_image = pygame.image.load(hit_image_path)
        self.fire_speed = 5
        self.fire_volume = fire_volume
        self.shot_sound.set_volume(self.fire_volume)
        self.fires = []
        self.screen = screen
        self.hit_image_path = hit_image_path
        self.was_hit = False
        self.lives = lives
        self.remaining_lives = lives
        self.hit_timer = None
        self.next_hit_timer = None
        self.time_to_get_out_of_hit_state = 600
        self.hit_sound_path = hit_sound_path
        if self.hit_sound_path is not None:
            self.hit_sound = pygame.mixer.Sound(self.hit_sound_path)
            self.hit_sound.set_volume(0.8)

    def draw(self, custom_image = None):
        if custom_image is None:
            self.screen.blit(self.image, (self.x_position, self.y_position))
        else:
            self.screen.blit(custom_image, (self.x_position, self.y_position))
        self.verify_hit_state()

    def destroy(self):
        pass

    @abstractmethod
    def draw_fires(self):
        pass

    @abstractmethod
    def handle_wall_collisions(self):
        pass

    @abstractmethod
    def handle_x_movements(self, keys=None):
        pass

    @abstractmethod
    def handle_shot(self, keys=None):
        pass

    def change_to_hit_image(self):
        self.image = self.hit_image
        self.hit_timer = pygame.time.get_ticks() + self.time_to_get_out_of_hit_state


    def change_to_original_image(self):
        self.image = self.original_image

    def verify_hit_state(self):
        if self.hit_timer is not None and pygame.time.get_ticks() >= self.hit_timer:
            self.change_to_original_image()
            self.hit_timer = None

    def decrease_player_lives(self):
        if(self.remaining_lives > 0):
           self.remaining_lives-=1
        else:
            from src.game import Game
            game = Game.get_instance()
            game.change_scene(ScenesEnum.TRY_AGAIN_SCENE)


    def handle_hit(self):
        is_not_being_hit = self.hit_timer is None and self.image == self.original_image
        if is_not_being_hit :
            self.decrease_player_lives()
            self.change_to_hit_image()
            if self.hit_sound_path is not None:
                self.play_hit_sound()

    def play_hit_sound(self):
        self.hit_sound.play()

    def get_width(self):
        return self.image.get_width()

    def get_height(self):
        return self.image.get_height()
