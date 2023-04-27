import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.bullet import Bullet

class Scene:
  def __init__(self, background_image, background_music, screen, player=None, enemy=None):
    pygame.mixer.init()
    self.background_image = background_image
    self.background_music = background_music
    self.background_music_volume = 0.5
    self.player = player
    self.enemy = enemy
    self.__screen = screen

  def draw(self):
    background_image_loaded = pygame.image.load(self.background_image)
    self.__screen.blit(background_image_loaded, (0, 0))
    if self.player is not None:
      self.player.draw()
    if self.enemy is not None:
      self.enemy.draw()

  def play_background_music(self, background_music_volume):
    background_music = pygame.mixer.Sound(self.background_music)
    background_music.set_volume(self.background_music_volume)
    background_music.play(-1)

