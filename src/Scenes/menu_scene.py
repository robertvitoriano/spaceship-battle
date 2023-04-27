from src.Scenes.scene import Scene
class MenuScene(Scene):
    def __init__(self, background_image, background_music, screen):
      super().__init__(background_image=background_image, background_music=background_music, screen=screen)
      self.background_image = background_image
      self.background_music = background_music
