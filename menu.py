import pygame
from config import DISPLAY

ARROW_POSITIONS = [
    ((DISPLAY["WIDTH"]* DISPLAY["MULTIPLIER"]) / 2 - 140 * DISPLAY["MULTIPLIER"], (DISPLAY["HEIGHT"]* DISPLAY["MULTIPLIER"]) / 2 - 18 * DISPLAY["MULTIPLIER"]),
    ((DISPLAY["WIDTH"]* DISPLAY["MULTIPLIER"]) / 2 - 140 * DISPLAY["MULTIPLIER"], (DISPLAY["HEIGHT"]* DISPLAY["MULTIPLIER"]) / 2 + 25 * DISPLAY["MULTIPLIER"]),



]


class Menu:
    
    def __init__(self):
        self.bg = pygame.transform.scale(pygame.image.load(
            "./assets/menu/bg.png"), (DISPLAY["WIDTH"]* DISPLAY["MULTIPLIER"],  DISPLAY["HEIGHT"]* DISPLAY["MULTIPLIER"]))
        self.arrow = pygame.transform.scale(pygame.image.load(
            "./assets/menu/selector.png"), (48* DISPLAY["MULTIPLIER"], 62* DISPLAY["MULTIPLIER"]))
        self.arrow_pos = 0 ; 
    def display_menu(self, screen):
        screen.blit(self.bg, (0, 0))

    def display_arrow(self, screen):
        screen.blit(self.arrow, ARROW_POSITIONS[self.arrow_pos])

    def update_arrow(self, dir):
        if (dir == "UP" and self.arrow_pos == 1):
            self.arrow_pos = 0
        elif (dir == "DOWN" and self.arrow_pos == 0):
            self.arrow_pos = 1;  

game_menu = Menu()
