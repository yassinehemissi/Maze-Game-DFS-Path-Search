import pygame
from config import DISPLAY


class Player:
    x = 0
    y = 0

    skin = pygame.transform.scale(pygame.image.load(
        "./assets/skin4.png"), (32 * DISPLAY["MULTIPLIER"], 32 * DISPLAY["MULTIPLIER"]))

    def __init__(self, _x, _y):
        self.x = _x
        self.y = _y

    def update_position(self, maze_pos, _x, _y):
        if (maze_pos == 0):
            return False
        if (maze_pos == "T" or maze_pos == "E"):
            return True
        self.x = _x
        self.y = _y
        return False

    def display_player(self, screen):
        screen.blit(
            self.skin, ((self.x + 1) * 32 * DISPLAY["MULTIPLIER"], (self.y + 1) * 32 * DISPLAY["MULTIPLIER"]))


player = Player(0, 0)
