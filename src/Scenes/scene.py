import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.fire import Fire


class Scene():
  def __init__(self, background_image, background_music, screen, player=None, background_music_volume = 0.4, background_speed = 0):
    pygame.mixer.init()
    self.background_music = background_music
    self.background_music_volume = background_music_volume
    self.player = player
    self.__screen = screen
    self.background_music_loaded = None
    self.background_speed = background_speed

    background_image_loaded = pygame.image.load(background_image)
    self.background_image_scalled = pygame.transform.scale(background_image_loaded, (self.__screen.get_width(),self.__screen.get_height()))
    self.background_y = 0

  def draw(self):
    self.background_y+=self.background_speed
    self.__screen.blit(self.background_image_scalled, (0, self.background_y))
    self.__screen.blit(self.background_image_scalled, (0, -self.__screen.get_height()+self.background_y))


    if(self.background_y == self.__screen.get_height()):
      self.background_y = 0
    if self.player is not None:
      self.player.draw()


  def play_background_music(self, background_music_volume):
    self.background_music_loaded = pygame.mixer.Sound(self.background_music)
    self.background_music_loaded.set_volume(self.background_music_volume)
    self.background_music_loaded.play(-1)

  def stop_background_music(self):
    self.background_music_loaded.stop()


  def handle_scene_events(self, events, keys = None):
    pass
