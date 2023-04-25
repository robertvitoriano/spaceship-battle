import  pygame

# Initialize the Pygame
pygame.init()
pygame.mixer.init()

#GAME SETTINGS
WIDTH = 800
HEIGHT = 600
running = True
background_music_volume = 0.3
background_music = pygame.mixer.Sound('background.wav')
background_music.set_volume(background_music_volume)
background_music.play(-1)

# create the screen
pygame.display.set_caption("Space Invaders")
background_image = pygame.image.load("background.png")
screen = pygame.display.set_mode((WIDTH,HEIGHT))




# Player
speed = 0
player_speed_rate = 8
player_right_collision = False
player_left_collision = False
player_image = pygame.image.load('./player.png')
player_x_coordinate = WIDTH/2 - player_image.get_width()
player_x_position = player_x_coordinate
player_y_position = HEIGHT - 100
player_shot_sound = pygame.mixer.Sound('laser.wav')
bullet_image = pygame.image.load('./bullet.png')
bullet_speed = 5
bullets = []

def draw_player(x, y):
    screen.blit(player_image,(x, y))

def render():
    screen.blit(background_image, (0, 0))
    handle_actions()
    handle_player_wall_collisions()
    pygame.display.update()

def handle_actions():
    keys = pygame.key.get_pressed()
    handle_player_x_movements(keys)
    handle_player_shot(keys)
    handle_bullets()
    draw_player(player_x_position, player_y_position)

def handle_player_wall_collisions():
    global player_right_collision
    global player_left_collision
    global player_x_position
    if player_x_position >= WIDTH - player_image.get_width():
        player_right_collision = True
    else:
        player_right_collision = False

    if player_x_position <= 0:
       player_left_collision = True
    else:
        player_left_collision = False

def handle_player_x_movements(keys):
    global speed
    global player_x_position

    if keys[pygame.K_LEFT] and not player_left_collision:
       speed-=player_speed_rate

    if keys[pygame.K_RIGHT] and not player_right_collision:
       speed+=player_speed_rate

    player_x_position =  player_x_coordinate + speed


def handle_player_shot(keys):
    global player_y_position
    if keys[pygame.K_SPACE]:
        global HEIGHT
        player_shot_sound.play()
        bullet_y_position = player_y_position
        bullet_x_position = player_x_position + player_image.get_width()/2 - bullet_image.get_width()/2
        bullets.append((bullet_x_position, bullet_y_position))

def handle_bullets():
    global bullets
    new_bullets = []

    for bullet in bullets:
        bullet_x_position, bullet_y_position = bullet
        bullet_y_position -= bullet_speed
        if bullet_y_position > 0:
            screen.blit(bullet_image, (bullet_x_position, bullet_y_position))
            new_bullets.append((bullet_x_position, bullet_y_position))
        else:
            pass
    bullets = new_bullets


while running:
    render()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


