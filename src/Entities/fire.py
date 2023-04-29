import pygame
class Fire(pygame.sprite.Sprite):
    def __init__(self, x, y, direction,fire_image, rect = None, screen = None ):
        self.x_position = x
        self.y_position = y
        self.speed = 5
        self.direction = direction
        self.fire_image = fire_image
        self.screen = screen
        self.image = self.screen.blit(self.fire_image,(x, y))
        self.rect = pygame.Rect(x, y, fire_image.get_width(), fire_image.get_height())



    def update(self):
        self.y_position += self.speed * self.direction

    def draw(self, new_x_position, new_y_position):
        self.image = self.screen.blit(self.fire_image,(new_x_position, new_y_position))
        self.rect = pygame.Rect(new_x_position, new_y_position, self.fire_image.get_width(), self.fire_image.get_height())

