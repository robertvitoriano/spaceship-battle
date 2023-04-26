import pygame
from src.Entities.player import Player
from src.Entities.enemy import Enemy

class Game:
    def __init__(self):
        self.running = False
        self.clock = pygame.time.Clock()
        self.FPS = 60
        self.width, self.height = 800, 600
        self.screen = None
        self.background_music_volume = 0.1
        self.background_music = None
        self.player = None
        self.enemy = None

    def init(self):
        pygame.init()
        pygame.mixer.init()
        self.running = True

        # create the screen
        pygame.display.set_caption("Space Invaders")
        self.screen = pygame.display.set_mode((self.width, self.height))

        # set up background music
        self.background_music = pygame.mixer.Sound('assets/music/background.wav')
        self.background_music.set_volume(self.background_music_volume)
        self.background_music.play(-1)

        # create game objects
        self.player = Player(self.screen,
                             'assets/images/player.png',
                             'assets/music/laser.wav',
                             'assets/images/bullet.png')
        self.enemy = Enemy(self.screen,
                           'assets/images/enemy.png',
                           'assets/music/laser.wav',
                           'assets/images/bullet.png')

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        keys = pygame.key.get_pressed()

        self.player.handle_x_movements(keys)
        self.player.handle_wall_collisions()
        self.player.handle_shot(keys)

        self.player.handle_bullets()

        self.enemy.handle_x_movements(keys)
        self.enemy.handle_wall_collisions()

    def draw(self):
        # draw background
        background_image = pygame.image.load("assets/images/background.png")
        self.screen.blit(background_image, (0, 0))

        # draw game objects
        self.player.draw()
        self.enemy.draw()

        # update display
        pygame.display.update()

    def stop(self):
        self.running = False

    def run(self):
        self.init()

        while self.running:
            self.handle_events()
            self.update()
            self.draw()

            self.clock.tick(self.FPS)

        # shut down all Pygame modules
        pygame.quit()
