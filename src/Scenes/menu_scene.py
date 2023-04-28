from src.Scenes.scene import Scene
from src.Scenes.ui_components.quit_button import QuitButton
from src.Scenes.ui_components.start_game_button import StartGameButton

import pygame
class MenuScene(Scene):
    def __init__(self, background_image, background_music, screen):
      super().__init__(background_image=background_image, background_music=background_music, screen=screen)
      self.background_image = background_image
      self.background_music = background_music
      self.screen = screen
      self.start_game_button = StartGameButton(screen=self.screen,width=300, height=50,x=200, y=200, color=(255, 0, 0), title="Start Game")
      self.quit_button = QuitButton(screen=self.screen,width=300, height=50,x=200, y=400, color=(255, 0, 0), title="Quit Game")

    def draw(self):
      super().draw()
      self.quit_button.draw()
      self.start_game_button.draw()

    def handle_scene_events(self, event):
      self.start_game_button.handle_button_events(event)
      self.quit_button.handle_button_events(event)
