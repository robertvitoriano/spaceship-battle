import pygame
from src.Scenes.ui_components.button import Button
from src.game import Game
from src.Scenes.button_enum import ButtonsEnum

class QuitButton(Button):
  def __init__(self, screen, width, height,x,y, color, title):
    super().__init__(screen=screen,width=width, height=height,x=x,y=y, color=color, title=title)

  def handle_button_events(self, event):
    if event.type == pygame.MOUSEBUTTONDOWN:
      button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
      if button_rect.collidepoint(pygame.mouse.get_pos()) and event.button == ButtonsEnum.LEFT_MOUSE_BUTTON.value:
        game = Game.get_instance()
        game.quit_game()
