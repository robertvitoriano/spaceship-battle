from src.Scenes.scene import Scene

import pygame
class MenuScene(Scene):
    def __init__(self, background_image, background_music, screen):
      super().__init__(background_image=background_image, background_music=background_music, screen=screen)
      self.background_image = background_image
      self.background_music = background_music
      self.screen = screen

    def create_quit_button(self):
      quit_button = pygame.Surface((100, 50))
      pygame.draw.rect(quit_button, (255, 0, 0), (0, 0, 100, 50))
      quit_button_pos = (50, 50)
      self.screen.blit(quit_button, quit_button_pos)

    def handle_scene_events(self, event):
      if event.type == pygame.MOUSEBUTTONDOWN:
        if quit_button.get_rect().move(quit_button_pos).collidepoint(pygame.mouse.get_pos()):
            running = False
