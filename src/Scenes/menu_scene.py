from src.Scenes.scene import Scene
from src.Scenes.ui_components.quit_button import QuitButton
from src.Scenes.ui_components.start_game_button import StartGameButton

import pygame
class MenuScene(Scene):
    def __init__(self, background_image, background_music, screen, background_music_volume, background_speed):
      super().__init__(background_image=background_image, background_music=background_music, screen=screen, background_music_volume=background_music_volume, background_speed=background_speed)
      self.background_image = background_image
      self.background_music = background_music
      self.screen = screen
      screen_width = screen.get_width()
      screen_height = screen.get_height()
      self.start_game_button = StartGameButton(screen=self.screen,width=300, height=50,x=screen_width/2 - 150, y=screen_height/3, color=(255, 0, 0), title="Start Game", hover_color=(0,0,0))
      self.quit_button = QuitButton(screen=self.screen,width=300, height=50,x=screen_width/2 - 150, y=screen_height/2, color=(255, 0, 0), title="Quit Game", hover_color=(0,0,0))

    def draw(self):
      super().draw()
      self.quit_button.draw()
      self.start_game_button.draw()

    def handle_scene_events(self, events, keys = None):
      self.start_game_button.handle_button_events(events)
      self.quit_button.handle_button_events(events)


