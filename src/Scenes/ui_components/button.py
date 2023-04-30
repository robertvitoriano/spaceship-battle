import pygame
from src.Scenes.button_enum import ButtonsEnum
from abc import ABC, abstractmethod

class Button(ABC):
  def __init__(self, screen, width, height,x, y, color, title, font_size=24,scene_to_go = None, hover_color=None):
    pygame.font.init()
    self.width = width
    self.height = height
    self.x = x
    self.y = y
    self.color = color
    self.title = title
    self.screen = screen
    self.button = None
    self.button_rect = None
    self.scene_to_go = scene_to_go

    self.font = pygame.font.SysFont(None, font_size)
    self.button = pygame.Surface((self.width, self.height))
    self.button.fill(self.color)
    self.draw_title()
    self.hovered = False
    self.hover_color = hover_color

  def draw(self):
    self.screen.blit(self.button, (self.x, self.y))


  def handle_button_events(self, event):
    pass

  def hover_button(self, event, is_hovering_button, hover_color = None):
    if event.type == pygame.MOUSEMOTION:
      if is_hovering_button and not self.hovered:
          pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
          self.hovered = True
          if self.hover_color is not None:
            self.button = pygame.Surface((self.width, self.height))
            self.button.fill(self.hover_color)
            self.draw_title()
      elif self.hovered:
          pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
          self.button = pygame.Surface((self.width, self.height))
          self.button.fill(self.color)
          self.screen.blit(self.button, (self.x, self.y))
          self.draw_title()
          self.hovered = False

  def get_button(self):
    return self.button

  def draw_title(self):
    text_surface = self.font.render(self.title, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.center = (self.width / 2, self.height / 2)
    self.button.blit(text_surface, text_rect)

