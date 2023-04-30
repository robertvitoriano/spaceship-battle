import pygame
from src.Scenes.ui_components.button import Button
from src.Scenes.button_enum import ButtonsEnum

class QuitButton(Button):
    def __init__(self, screen, width, height, x, y, color, title, hover_color=None):
        super().__init__(screen=screen, width=width, height=height, x=x, y=y, color=color, title=title, hover_color=hover_color)

    def handle_button_events(self, events):
        from src.game import Game

        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        is_hovering_button = button_rect.collidepoint(pygame.mouse.get_pos())
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_hovering_button and event.button == ButtonsEnum.LEFT_MOUSE_BUTTON.value:
                    game = Game.get_instance()
                    game.quit_game()

            self.hover_button(event, is_hovering_button)


