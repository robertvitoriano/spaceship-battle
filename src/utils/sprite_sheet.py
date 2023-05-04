class Spritesheet:
 def __init__(self, spritesheet_image):
   self.spritesheet_image = spritesheet_image

def get_sprite(self, width, height, frame_index=0,background_color=None, scale=1):
  sprite = pygame.Surface((width, height)).convert_alpha()
  sprite.blit(self.spritesheet_image, (0,0), area=((width * height),0, width, height))
  scaled_sprite = pygame.transform.scale(sprite, width*scale, height*scale)
  if(background_color is not None):
    scaled_sprite.set_colorkey(background_color)

  return scaled_sprite
  pass
