from src.Scenes.scene import Scene
from src.Scenes.ui_components.quit_button import QuitButton
import pygame
class MenuScene(Scene):
    def __init__(self, background_image, background_music, screen):
      super().__init__(background_image=background_image, background_music=background_music, screen=screen)
      self.background_image = background_image
      self.background_music = background_music
      self.screen = screen
      self.quit_button = QuitButton(screen=self.screen,width=100, height=50,x=50, y=50, color=(255, 0, 0), title="MENU")

    def draw(self):
      super().draw()
      self.quit_button.draw()
