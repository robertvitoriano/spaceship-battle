import pygame
from src.Scenes.button_enum import ButtonsEnum
from src.game import Game
from abc import ABC, abstractmethod

class Button(ABC):
  def __init__(self, screen, width, height,x, y, color, title):
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.color = color
    self.title = title
    self.screen = screen
    self.button = None
    self.button_rect = None

  def draw(self):
    self.button = pygame.Surface((self.width, self.height))
    self.button_rect = pygame.draw.rect(self.button, self.color , (0, 0, self.width, self.height))

    self.screen.blit(self.button, (self.x, self.y))

  @abstractmethod
  def handle_button_events(self):
    pass

  def get_button(self):
    return self.button
