import pygame
import time

from src.Entities.player import Player
from src.Entities.enemy import Enemy
from src.Entities.fire import Fire
from src.Scenes.scenes_enum import ScenesEnum
from src.Scenes.menu_scene import MenuScene
from src.Scenes.first_scene import FirstScene
from src.Scenes.try_again_scene import TryAgainScene
from src.Scenes.game_won_scene import GameWonSCene

game = None

class Game:
    def __init__(self, scenes, starting_scene, main_volume, screen):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()


        self.scenes = scenes
        self.current_scene = starting_scene

        self.running = True
        self.clock = pygame.time.Clock()
        self.FPS = 60

        self.width, self.height = 800, 600
        self.main_volume = main_volume

        self.screen = screen
        self.mouse_image = pygame.transform.scale(pygame.image.load('assets/images/custom_mouse_pointer.png'),(50,50))
        self.is_paused = False
        self.pause_font = pygame.font.Font(None, 50)
        pygame.mouse.set_visible(False)

    def draw_cursor(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()

        self.screen.blit(self.mouse_image,( mouse_x, mouse_y))

    @classmethod
    def get_instance(cls, scenes=None, starting_scene = 0, main_volume = 0.4, screen = None):
        global game
        if game is None and scenes is not None:
            game = Game(scenes=scenes, starting_scene=starting_scene, main_volume=main_volume, screen=screen)
        return game

    def change_scene(self, new_scene_number):
        self.scenes[self.current_scene].stop_background_music()
        self.current_scene = new_scene_number
        self.scenes[self.current_scene].play_background_music(self.main_volume)

    def update(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        self.scenes[self.current_scene].handle_scene_events(events,keys)
        for event in events:
            if event.type == pygame.QUIT:
                self.quit_game()

    def draw(self):
        self.scenes[self.current_scene].draw()
        self.draw_cursor()

        pygame.display.update()


    def stop(self):
        self.running = False

    def quit_game(self):
        self.stop()

    def restart_game(self):
        self.scenes[self.current_scene].stop_background_music()
        global game
        WIDTH=1366

        HEIGHT=720

        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Space Invaders")
        main_volume = 0.3


        player = Player(screen,
                        image_path='assets/images/player.png',
                        shot_sound_path='assets/music/laser.wav',
                        fire_image_path='assets/images/player_laser.png',
                        hit_image_path='assets/images/player_hit.png',
                        live_image_path='assets/images/heart_image.png',
                        hit_sound_path="assets/music/player_impact.wav",
                        fire_volume=0.4,
                        lives=5)


        scenes = {
            ScenesEnum.MENU_SCENE: MenuScene(background_image="assets/images/menu_background.jpg",
                                            background_music="assets/music/infected_vibes_menu_music.mp3",
                                            screen=screen,background_music_volume=main_volume,
                                            background_speed=15),

            ScenesEnum.FIRST_SCENE: FirstScene(background_image="assets/images/background.png",
                                            background_music="assets/music/start.wav",
                                            screen=screen, player= player,
                                            background_music_volume=main_volume,
                                            background_speed=20),
            ScenesEnum.GAME_WON_SCENE: GameWonSCene(screen=screen, background_color=(0, 0, 0), background_music="assets/music/lose_background_music.wav", background_music_volume=main_volume),
            ScenesEnum.TRY_AGAIN_SCENE: TryAgainScene(screen=screen, background_color=(0, 0, 0), background_music="assets/music/lose_background_music.wav", background_music_volume=main_volume)
        }
        game = None
        game = self.get_instance(scenes, ScenesEnum.MENU_SCENE, main_volume=main_volume, screen=screen)

        # call the run method to start the game loop again
        game.run()


    def handle_pause(self):
        self.screen.fill((0,0,0))
        pause_text = self.pause_font.render("Paused", None, (255, 255, 255))
        text_width, text_height = pause_text.get_size()
        x = (self.screen.get_width() - text_width) // 2
        y = (self.screen.get_height() - text_height) // 2
        self.screen.blit(pause_text, (x, y))
        pygame.display.flip()

    def verify_pause(self):
        keys = pygame.key.get_pressed()
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.is_paused = not self.is_paused
                    if self.is_paused:
                        self.scenes[self.current_scene].stop_background_music()
                    else:
                        self.scenes[self.current_scene].play_background_music(self.main_volume)

    def run(self):
        self.scenes[self.current_scene].play_background_music(self.main_volume)

        while self.running:
            self.verify_pause()
            if not self.is_paused:
                self.draw()
                self.update()
            else:
                self.handle_pause()
            self.clock.tick(self.FPS)

        pygame.quit()
