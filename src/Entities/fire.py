import pygame
class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, direction,fire_image, rect = None,speed=50, screen = None, hit_volume = 0.4 ):
        super().__init__()
        self.x_position = x
        self.y_position = y
        self.speed = speed
        self.direction = direction
        scaled_fired_image = pygame.transform.scale(fire_image, (60,60))
        self.fire_image = pygame.transform.rotate(scaled_fired_image, 180)
        self.mask = pygame.mask.from_surface(self.fire_image)
        self.rect = pygame.Rect(self.x_position, self.y_position, self.fire_image.get_width(), self.fire_image.get_height())
        self.screen = screen
        self.rect = pygame.Rect(x, y, fire_image.get_width(), fire_image.get_height())
        self.hit_sound = pygame.mixer.Sound('assets/music/player_laser_hit_sound.mp3')
        self.hit_sound.set_volume(hit_volume)

    def update(self):
        self.y_position += self.speed * self.direction

    def play_hit_sound(self):
        self.hit_sound.play()

    def draw(self, new_x_position, new_y_position):
        self.image = self.screen.blit(self.fire_image,(new_x_position, new_y_position))
        self.rect = pygame.Rect(new_x_position, new_y_position, self.fire_image.get_width(), self.fire_image.get_height())


