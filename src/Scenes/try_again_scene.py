from src.Scenes.scene import Scene
from src.Scenes.ui_components.try_again_button import TryAgainButton
from src.Scenes.ui_components.quit_button import QuitButton
import pygame
class TryAgainScene(Scene):
  def __init__(self, background_color, background_music, background_music_volume, screen):
    super().__init__(background_color=background_color, screen=screen, background_music=background_music, background_music_volume=background_music_volume)
    self.try_again_button = TryAgainButton(color=(0,0,0),title="Try again!", height=50, width=300,x=screen.get_width()/2 - 150, y=screen.get_height()/2, screen=screen)
    self.quit_game_button = QuitButton(color=(0,0,0),title="Quit Game!", height=50, width=300,x=screen.get_width()/2 - 150, y=screen.get_height()/3, screen=screen)



  def draw(self):
    super().draw()
    self.try_again_button.draw()
    self.quit_game_button.draw()

  def handle_scene_events(self,events, keys = None):
    self.try_again_button.handle_button_events(events)
    self.quit_game_button.handle_button_events(events)



