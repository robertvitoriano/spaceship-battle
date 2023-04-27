from src.Scenes.ui_components.button import Button
from src.game import Game
import pygame

class QuitButton(Button):
  def __init__(self, screen, width, height,x,y, color, title):
    super().__init__(screen=screen,width=width, height=height,x=x,y=y, color=color, title=title)


  def handle_button_events(self):
    if event.type == pygame.MOUSEBUTTONDOWN:
      if super().button_rect.get_rect().move((0,0, self.width, self.height)).collidepoint(pygame.mouse.get_pos()) and event.button == ButtonsEnum.LEFT_MOUSE_BUTTON:
        Game.quit_game()
