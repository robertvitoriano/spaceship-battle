from src.Scenes.scene import Scene
from src.Entities.enemy import Enemy
from src.Scenes.scenes_enum import ScenesEnum
from src.Scenes.game_won_scene import GameWonSCene
import pygame
import random
import time
import os
import glob


class FirstScene(Scene):
    def __init__(self, background_image, background_music, screen, player, background_music_volume, background_speed):
        super().__init__(background_image=background_image, background_music=background_music, player=player, screen=screen, background_music_volume=background_music_volume, background_speed=background_speed)
        self.enemy_explosion_sprites = []
        explosion_folder_path = 'assets/images/explosion_animation_sprites'
        explosions_sprites_paths = glob.glob(os.path.join(explosion_folder_path, '*'))
        self.load_enemy_explosion_sprites(explosions_sprites_paths)

        self.background_image = background_image
        self.background_music = background_music
        self.player = player
        self.screen = screen
        self.dificult_y_rate = 45
        self.number_of_enemy_waves = random.randint(5, 15)
        self.max_number_of_enemies_per_waves = random.randint(20, 50)
        self.current_wave_index = 0
        self.quantities_per_wave = []
        self.get_quantities_per_wave()
        self.enemies_to_remove = []


    def draw(self):
        super().draw()
        self.draw_enemies_wave()
        self.player.draw_fires()
        self.player.draw_lives()
        self.check_enemies_to_remove()


    def get_current_wave_enemies(self):
        from src.game import Game

        enemies = []
        if self.current_wave_index == len(self.quantities_per_wave) - 1:
            game = Game.get_instance()
            game.change_scene(ScenesEnum.GAME_WON_SCENE)


        for i in range(0,self.quantities_per_wave[self.current_wave_index]):
            enemies.append(Enemy(
                self.screen,
                'assets/images/enemy.png',
                'assets/music/laser.wav',
                'assets/images/bullet.png',
                'assets/images/enemy_hit_image.png',
                0.1,
                lives=2,
                id=i,
                dificult_y_rate= random.randint(10, self.dificult_y_rate),
                speed_rate=5,
                explosion_sprites=self.enemy_explosion_sprites
            ))

        return enemies

    def handle_scene_events(self, events, keys):
        self.handle_enemies_events(keys)
        self.handle_player_events(events, keys)

    def handle_player_events(self, events, keys):
        self.player.handle_x_movements(keys)
        self.player.handle_wall_collisions()
        self.player.handle_shot(keys)
        self.handle_enemy_collision_with_player()

    def handle_enemies_events(self, keys):
        for enemy in self.enemies:
            enemy.handle_x_movements(keys)
            enemy.handle_wall_collisions()
            if(enemy.is_enemy_out_screen()):
                self.enemies.remove(enemy)
        self.handle_enemy_hit()

    def draw_enemies_wave(self):
        if(len(self.enemies) == 0):
            self.current_wave_index += 1
            self.enemies = self.get_current_wave_enemies()
        for enemy in self.enemies:
            enemy.draw()


    def handle_enemy_hit(self):
        fires = self.player.get_fires()
        enemy_group = pygame.sprite.Group(self.enemies)
        for i, fire in enumerate(fires):
            collisions = pygame.sprite.spritecollide(fire, enemy_group, True)
            for enemy in collisions:
                self.enemies_to_remove.append(enemy)
                enemy.handle_hit()
                self.player.remove_fire(i)
                fire.play_hit_sound()

    def handle_enemy_collision_with_player(self):
        enemy_group = pygame.sprite.Group(self.enemies)
        enemy_player_collisions = pygame.sprite.spritecollide(self.player, enemy_group, True)
        for enemy in enemy_player_collisions:
            self.player.handle_hit()


    def get_quantities_per_wave(self):
        quantities_per_wave = []
        for i in range(0,self.number_of_enemy_waves):
            self.quantities_per_wave.append(random.randint(1, self.max_number_of_enemies_per_waves))
        self.enemies = self.get_current_wave_enemies()


    def should_remove_enemy(self):
        self.time_to_get_out_of_hit_state

    def check_enemies_to_remove(self):
        for enemy in self.enemies_to_remove:
            if(enemy.should_remove_enemy()):
                if enemy in self.enemies:
                    self.enemies.remove(enemy)

    def load_enemy_explosion_sprites(self, explosions_sprites_paths):
        for explosion_sprite_path in explosions_sprites_paths:
            self.enemy_explosion_sprites.append(pygame.image.load(explosion_sprite_path))

