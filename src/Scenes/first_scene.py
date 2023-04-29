from src.Scenes.scene import Scene
from src.Entities.enemy import Enemy
import pygame

class FirstScene(Scene):
    def __init__(self, background_image, background_music, screen, player, background_music_volume):
        super().__init__(background_image=background_image, background_music=background_music, player=player, screen=screen, background_music_volume=background_music_volume)
        self.background_image = background_image
        self.background_music = background_music
        self.player = player
        self.screen = screen
        self.enemies = self.get_enemies()
        self.dificult_y_rate = 10

    def draw(self):
        super().draw()
        self.draw_enemies()
        self.player.draw_fires()
        self.player.draw_lives()


    def get_enemies(self):
        enemies = []
        for i in range(0,10):
            enemies.append(Enemy(
                self.screen,
                'assets/images/enemy.png',
                'assets/music/laser.wav',
                'assets/images/bullet.png',
                'assets/images/player_hit.png',
                0.1,
                life=10,
                id=i,
                dificult_y_rate=10
            ))

        return enemies

    def handle_scene_events(self, events, keys):
        self.handle_enemies_events(keys)
        self.handle_player_events(events, keys)

    def handle_player_events(self, events, keys):
        self.player.handle_x_movements(keys)
        self.player.handle_wall_collisions()
        self.player.handle_shot(keys)

    def handle_enemies_events(self, keys):
        for enemy in self.enemies:
            enemy.handle_x_movements(keys)
            enemy.handle_wall_collisions()
            if(enemy.is_enemy_out_screen()):
                self.enemies.remove(enemy)
                self.player.decrease_lives()
        self.handle_enemy_hit()

    def draw_enemies(self):
        for enemy in self.enemies:
            enemy.draw()


    def handle_enemy_hit(self):
        fires = self.player.get_fires()
        enemy_group = pygame.sprite.Group(self.enemies)
        for i, fire in enumerate(fires):
            collisions = pygame.sprite.spritecollide(fire, enemy_group, True)
            for enemy in collisions:
                self.player.remove_fire(i)
                fire.play_hit_sound()
                self.enemies.remove(enemy)

