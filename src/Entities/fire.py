import pygame
class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, direction,fire_image, rect = None, screen = None, hit_volume = 0.4 ):
        self.x_position = x
        self.y_position = y
        self.speed_rate = 100
        self.direction = direction
        self.fire_image = fire_image
        self.mask = pygame.mask.from_surface(fire_image)
        self.screen = screen
        self.image = self.screen.blit(self.fire_image,(x, y))
        self.rect = pygame.Rect(x, y, fire_image.get_width(), fire_image.get_height())
        self.hit_sound = pygame.mixer.Sound('assets/music/player_laser_hit_sound.mp3')
        self.hit_sound.set_volume(hit_volume)

    def update(self):
        self.y_position += self.speed_rate * self.direction

    def play_hit_sound(self):
        self.hit_sound.play()

    def draw(self, new_x_position, new_y_position):
        self.image = self.screen.blit(self.fire_image,(new_x_position, new_y_position))
        self.rect = pygame.Rect(new_x_position, new_y_position, self.fire_image.get_width(), self.fire_image.get_height())


