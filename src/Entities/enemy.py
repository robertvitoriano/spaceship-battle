from src.Entities.spaceship import Spaceship
import pygame
import random
class Enemy(Spaceship):
    def __init__(self, screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, id,lives = 2, dificult_y_rate = 2, speed_rate=5, explosion_sprites = []):
        super().__init__(screen, image_path, shot_sound_path, fire_image_path, hit_image_path, fire_volume, lives = lives, speed_rate=speed_rate)
        self.x_position = random.randint(0, self.screen_width - self.image.get_width())
        self.id = id
        self.y_position = 0
        self.direction = 1
        self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())
        self.speed_rate_y = 5 * dificult_y_rate
        self.is_out_screen = False
        self.point_to_get_down = random.randint(0, self.image.get_width())
        self.should_remove = False
        self.explosion_sprites=explosion_sprites
        self.time_per_explosion_sprite = int(self.time_to_get_out_of_hit_state/len(self.explosion_sprites))

    def handle_wall_collisions(self):
        if self.x_position <= 0 or self.x_position >= self.screen_width - self.image.get_width():
            self.direction = self.direction * -1
            self.y_position += self.speed_rate_y

    def handle_shot(self, keys=None):

        pass

    def draw_fires(self):
        pass

    def handle_x_movements(self, keys=None):
        is_not_being_hit = self.hit_timer is None and self.image == self.original_image
        if is_not_being_hit:
            self.x_position += self.speed_rate * self.direction
            self.rect = pygame.Rect(self.x_position, self.y_position, self.image.get_width(), self.image.get_height())

        self.handle_gone_out_screen()


    def handle_gone_out_screen(self):
        if self.y_position >= self.screen.get_height():
            self.is_out_screen = True

    def is_enemy_out_screen(self):
        return self.is_out_screen

    def get_enemy_id(self):
        return self.id

    def handle_hit(self):
        is_not_being_hit = self.hit_timer is None and self.image == self.original_image
        if is_not_being_hit :
            self.change_to_hit_image()
            self.draw_explosion_animation()


    def verify_hit_state(self):
        if self.hit_timer is not None and pygame.time.get_ticks() >= self.hit_timer:
            self.hit_timer = None
            self.should_remove = True

    def draw_explosion_animation(self):
        # Create an explosion animation sprite
        explosion_animation = pygame.sprite.Sprite()

        # Set the image to the first explosion sprite
        explosion_animation.image = self.explosion_sprites[0]

        # Set the rect to the same size and position as the enemy sprite
        explosion_animation.rect = self.rect

        # Create an animation group and add the explosion animation sprite to it
        explosion_group = pygame.sprite.Group(explosion_animation)

        # Set the frame rate of the animation
        frame_rate = 60

        # Calculate the duration of each explosion sprite
        explosion_duration = self.time_to_get_out_of_hit_state / len(self.explosion_sprites)

        # Create a timer to control the animation
        explosion_timer = 0

        # Loop until the animation is complete
        while explosion_timer < self.time_to_get_out_of_hit_state:
            # Get the time since the last frame (in milliseconds)
            dt = pygame.time.Clock().tick(frame_rate)

            # Update the explosion animation sprite
            explosion_animation.image = self.explosion_sprites[int(explosion_timer // explosion_duration)]
            explosion_animation.rect = self.rect

            # Draw the enemy and the explosion animation on the screen
            self.draw()
            explosion_group.draw(self.screen)

            # Update the screen
            pygame.display.flip()

            # Increment the timer
            explosion_timer += dt

        # Remove the explosion animation from the group
        explosion_group.remove(explosion_animation)

        # Reset the image to the default after the animation is complete
        self.image = self.original_image



    def should_remove_enemy(self):
        return self.should_remove


