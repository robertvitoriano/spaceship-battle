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
        self.background_image = background_image
        self.background_music = background_music
        self.player = player
        self.screen = screen

        self.enemy_explosion_sprites = []
        explosion_folder_path = 'assets/images/explosion_animation_sprites'
        explosions_sprites_paths = glob.glob(os.path.join(explosion_folder_path, '*'))
        self.load_enemy_explosion_sprites(explosions_sprites_paths)

        self.dificult_y_rate = 20
        self.number_of_enemy_waves = 5
        self.max_number_of_enemies_per_row = 4 #self.screen.get_width()//int(self.player.image.get_width()*2)
        self.current_wave_index = 0
        self.quantities_per_wave_row = []
        self.enemy_rows_per_wave = 5
        self.enemy_columns_per_wave = 5
        self.score_font = pygame.font.SysFont(None, 35)

        self.get_quantities_per_wave_row()
        self.enemies_to_remove = []

    def draw(self):
        super().draw()
        self.draw_enemies_wave()
        self.check_enemies_to_remove()

    def get_current_wave_enemies(self):
        from src.game import Game

        enemies = []
        if self.current_wave_index == len(self.quantities_per_wave_row) - 1 and len(self.enemies) == 0:
            game = Game.get_instance()
            game.change_scene(ScenesEnum.GAME_WON_SCENE)

        for i in range(0,5):
            for j in range(0,self.quantities_per_wave_row[self.current_wave_index]):
                enemies.append(Enemy(
                    self.screen,
                    image_path='assets/images/enemy.png',
                    shot_sound_path='assets/music/laser.wav',
                    fire_image_path='assets/images/bullet.png',
                    hit_image_path='assets/images/enemy_hit_image.png',
                    fire_volume=0.4,
                    lives=2,
                    id=i,
                    speed_rate=10,
                    explosion_sprites=self.enemy_explosion_sprites,
                    x_position= (self.player.image.get_width()+100)*i,
                    y_position= self.player.image.get_height()*j + self.player.image.get_height()
                ))

        return enemies

    def handle_scene_events(self, events, keys):
        self.handle_enemies_events(keys)
        self.handle_player_events(events, keys)

    def handle_player_events(self, events, keys):
        self.player.handle_x_movements(keys)
        self.player.handle_y_movements(keys)
        self.player.handle_wall_collisions()
        self.player.handle_shot(keys)
        self.handle_enemy_collision_with_player()

    def handle_enemies_events(self, keys):
        for enemy in self.enemies:
            if enemy.get_x_position() == self.player.get_x_position():
                enemy.handle_shot()
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
        from src.game import Game
        game = Game.get_instance()
        fires = self.player.get_fires()
        enemy_group = pygame.sprite.Group(self.enemies)
        for i, fire in enumerate(fires):
            collided_enemies = pygame.sprite.spritecollide(fire, enemy_group, True)
            if len(collided_enemies) > 0:
                collided_enemy = collided_enemies[0]
                self.player.remove_fire(i)
                game.increase_score()
                self.enemies_to_remove.append(collided_enemy)
                fire.play_hit_sound()
                collided_enemy.handle_hit()

    def handle_enemy_collision_with_player(self):
        for enemy in self.enemies:
            enemy_offset = (enemy.rect.topleft[0] - self.player.rect.topleft[0], enemy.rect.topleft[1] - self.player.rect.topleft[1])
            if self.player.mask.overlap(enemy.mask, enemy_offset):
                enemy.handle_hit()
                self.player.handle_hit()
                self.enemies_to_remove.append(enemy)


    def get_quantities_per_wave_row(self):
        quantities_per_wave_row = []
        for i in range(0,self.number_of_enemy_waves):
            self.quantities_per_wave_row.append(random.randint(0,self.max_number_of_enemies_per_row))
        self.enemies = self.get_current_wave_enemies()

    def check_enemies_to_remove(self):
        for enemy in self.enemies_to_remove:
            if(enemy.should_remove_enemy()):
                if enemy in self.enemies:
                    if enemy.get_out_of_screen():
                        self.player.decrease_player_lives()
                    self.enemies.remove(enemy)

    def load_enemy_explosion_sprites(self, explosions_sprites_paths):
        for explosion_sprite_path in explosions_sprites_paths:
            loaded_sprite = pygame.image.load(explosion_sprite_path)
            sprite = pygame.transform.scale(loaded_sprite, (self.player.get_width(), self.player.get_height()))

            self.enemy_explosion_sprites.append(sprite)

