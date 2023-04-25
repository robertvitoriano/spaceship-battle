import  pygame

# Initialize the Pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

running = True
speed = 0
player_speed_rate = 8
player_right_collision = False
player_left_collision = False
# create the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")
background_image = pygame.image.load("background.png")

# Player
player_image = pygame.image.load('./player.png')
player_x_coordinate = WIDTH/2 - player_image.get_width()
player_x_position = player_x_coordinate
player_y_position = HEIGHT - 100

def draw_player(x, y):
    screen.blit(player_image,(x, y))

def render():
    screen.blit(background_image, (0, 0))
    handle_movements()
    handle_player_wall_collisions()
    pygame.display.update()

def handle_movements():
    keys = pygame.key.get_pressed()
    handle_player_x_movements(keys)
    draw_player(player_x_position, player_y_position)

def handle_player_wall_collisions():
    global player_right_collision
    global player_left_collision
    global player_x_position
    print(player_x_position)
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

while running:

    render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


