import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.fire import Fire


class Scene():
  def __init__(self, background_image=None, background_music=None, screen=None, player=None, background_music_volume = 0.4, background_speed = 0,  background_color = None):
    pygame.mixer.init()
    pygame.font.init()
    self.background_music = background_music
    self.background_music_volume = background_music_volume
    self.player = player
    self.screen = screen
    self.background_music_loaded = pygame.mixer.Sound(self.background_music)
    self.background_speed = background_speed
    self.background_y = 0
    self.background_color = background_color
    self.background_image = None
    self.score_font = pygame.font.SysFont(None, 35)
    if background_image is not None:
      background_image_loaded = pygame.image.load(background_image)
      self.background_image_scalled = pygame.transform.scale(background_image_loaded, (self.screen.get_width(),self.screen.get_height()))

  def draw(self):
    if self.background_image is not None:
      self.background_y+=self.background_speed
      self.screen.blit(self.background_image_scalled, (0, self.background_y))
      self.screen.blit(self.background_image_scalled, (0, -self.screen.get_height()+self.background_y))
      if(self.background_y == self.screen.get_height()):
        self.background_y = 0
      if self.player is not None:
        self.player.draw()
    else:
      self.screen.fill(self.background_color)
    self.draw_score()

  def play_background_music(self, background_music_volume):
    self.background_music_loaded.set_volume(self.background_music_volume)
    self.background_music_loaded.play(-1)

  def stop_background_music(self):
    self.background_music_loaded.stop()

  def draw_score(self):
    from src.game import Game
    game = Game.get_instance()
    score_surface = self.score_font.render("SCORE: " + str(game.get_score()), True, (255, 255, 255))
    score_rect = score_surface.get_rect()
    score_rect.center = (self.screen.get_width() - 100, score_surface.get_height() + score_surface.get_height()/2 )
    self.screen.blit(score_surface, score_rect)

  def handle_scene_events(self, events, keys = None):

    pass
