import pygame
from abc import ABC, abstractmethod



class Spaceship(ABC):
    def __init__(self,
                 screen,
                 image_path,
                 shot_sound_path,
                 bullet_image_path,
                 bullet_volume
                 ):
        pygame.mixer.init()
        info = pygame.display.Info()
        self.screen_width = info.current_w
        self.screen_height = info.current_h
        self.speed = 0
        self.speed_rate = 8
        self.right_collision = False
        self.left_collision = False
        self.image = pygame.image.load(image_path)
        self.x_position = self.screen_width/2 - self.image.get_width()
        self.y_position = self.screen_height - 100
        self.shot_sound = pygame.mixer.Sound(shot_sound_path)
        self.bullet_image = pygame.image.load(bullet_image_path)
        self.bullet_speed = 5
        self.bullet_volume = bullet_volume
        self.shot_sound.set_volume(self.bullet_volume)
        self.bullets = []
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (self.x_position, self.y_position))

    @abstractmethod
    def draw_bullets(self):
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
