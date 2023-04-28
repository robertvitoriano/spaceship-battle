import pygame

class Entity(pygame.sprite.Sprite):
  def __init__(self, x, y, height, width, image):
    self.x = x
    self.y = y
    self.height = height
    self.width = width
    self.image = pygame.Surface((width, height))


  def draw(self):
    pass

