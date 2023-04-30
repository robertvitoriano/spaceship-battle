import pygame
from src.Scenes.button_enum import ButtonsEnum
from abc import ABC, abstractmethod

class Button(ABC):
  def __init__(self, screen, width, height,x, y, color, title, font_size=24,scene_to_go = None):
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

    font = pygame.font.SysFont(None, font_size)
    text_surface = font.render(title, True, (255, 255, 255))

    text_rect = text_surface.get_rect()
    text_rect.center = (width / 2, height / 2)

    self.button = pygame.Surface((self.width, self.height))
    self.button.fill(self.color)
    self.button.blit(text_surface, text_rect)
    self.hovered = False

  def draw(self):
    self.screen.blit(self.button, (self.x, self.y))


  def handle_button_events(self, event):
    pass

  def hover_button(self, event, is_hovering_button):
    if event.type == pygame.MOUSEMOTION:
      if is_hovering_button and not self.hovered:
          pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
          self.hovered = True
      elif self.hovered:
          pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
          self.hovered = False

  def get_button(self):
    return self.button
