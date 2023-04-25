import  pygame

# Initialize the Pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

running = True
speed = 0
player_speed_rate = 3

# create the screen
screen = pygame.display.set_mode((WIDTH,HEIGHT))

# Title and Icon
pygame.display.set_caption("Space Invaders")

# Player
player_image = pygame.image.load('./player.png')

player_x_coordinate = WIDTH/2 - player_image.get_width()

player_y_position = HEIGHT - 100
background_image = pygame.image.load("background.png")

def draw_player(x, y):
    screen.blit(player_image,(x, y))

def render():
    screen.blit(background_image, (0, 0))
    handle_movements()
    pygame.display.update()

def handle_movements():
    keys = pygame.key.get_pressed()
    player_x_position = get_player_x_position(keys)
    draw_player(player_x_position, player_y_position)


def get_player_x_position(keys):
    global speed

    if keys[pygame.K_LEFT]:
       speed-=player_speed_rate

    if keys[pygame.K_RIGHT]:
       speed+=player_speed_rate

    return player_x_coordinate + speed

while running:

    render()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


