# created by Allison Dixon
# last updated December 13, 2019
# this class creates a target and assigns its point values based on colors

import pygame, sys
from pygame.locals import *


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface
        self.score = 0

    def draw_target(self):
        x = int(self.main_surface.get_width()/2)
        y = int(self.main_surface.get_height()/2)
        pygame.draw.circle(self.main_surface, (255, 255, 254), (x, y), 200, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 200, 2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 160, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (x, y), 120, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (x, y), 80, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (x, y), 40, 0)

    def get_score(self, position):
        target_color = self.main_surface.get_at(position)
        if target_color == (255, 255, 0, 255):
            self.update_score(9)
        elif target_color == (225, 0, 0, 255):
            self.update_score(7)
        elif target_color == (0, 0, 255, 255):
            user_score = 5
        elif target_color == (0, 0, 0, 255):
            user_score = 3
        elif target_color == (255, 255, 254, 255):
            user_score = 1
        else:
            user_score = 0

    def update_score(self, score):
        self.score += score






        # mouse_font = pygame.font.SysFont("Helvetica", 32)
        # mouse_label = mouse_font.render(str(position), 1, (0, 0, 0))
        # self.main_surface.blit(mouse_label, (30, 30))

