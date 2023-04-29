from src.Scenes.scene import Scene
class FirstScene(Scene):
    def __init__(self, background_image, background_music, screen, player, enemy, background_music_volume):
        super().__init__(background_image=background_image, background_music=background_music, player=player, enemy=enemy, screen=screen, background_music_volume=background_music_volume)
        self.background_image = background_image
        self.background_music = background_music
        self.player = player
        self.enemy = enemy
