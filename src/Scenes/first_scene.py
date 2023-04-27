from src.Scenes.scene import Scene
class FirstScene(Scene):
    def __init__(self, background_image, background_music, screen, player, enemy):
        super().__init__(background_image=background_image, background_music=background_music, player=player, enemy=enemy, screen=screen)
        self.background_image = background_image
        self.background_music = background_music
        self.player = player
        self.enemy = enemy
