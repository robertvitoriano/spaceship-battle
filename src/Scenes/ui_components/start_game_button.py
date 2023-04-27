import pygame
from src.Scenes.ui_components.button import Button
from src.game import Game
from src.Scenes.button_enum import ButtonsEnum
from src.Scenes.scenes_enum import ScenesEnum


class StartGameButton(Button):
    def __init__(self, screen, width, height, x, y, color, title):
        super().__init__(screen=screen, width=width, height=height, x=x, y=y, color=color, title=title)

    def handle_button_events(self, event):
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        is_hovering_button = button_rect.collidepoint(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONDOWN:
            if is_hovering_button and event.button == ButtonsEnum.LEFT_MOUSE_BUTTON.value:
                game = Game.get_instance()
                game.change_scene(ScenesEnum.FIRST_SCENE)

        self.hover_button(event, is_hovering_button)


