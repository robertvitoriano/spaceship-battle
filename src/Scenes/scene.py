import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.bullet import Bullet
class Scene:
  def __init__(self, background_image, background_music, player = None, enemy = None):
    self.background_image = background_image
    self.scene_number = scene_number
    self.background_music = background_music
    self.player = player
    self.enemy = enemy


  def draw():
      background_image_loaded = pygame.image.load(self.background_image)
      screen.blit(self.background_image_loaded, (0, 0))
      if not None:
       player.draw()
      if not None:
       enemy.draw()

  def play_background_music():
     background_music = pygame.mixer.Sound('assets/music/background.wav')
     background_music.set_volume(background_music_volume)
     background_music.play(-1)


pygame.quit()
