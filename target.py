# created by Allison Dixon
# last updated December 13, 2019
# this class creates a target and assigns its point values based on colors

import pygame, sys
from pygame.locals import *


class Target:

    def __init__(self, main_surface):
        self.main_surface = main_surface

    def draw_target(self):
        x = self.main_surface.get_width()/2
        y = self.main_surface.get_height()/2
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 200, 2)
        pygame.draw.circle(self.main_surface, (0, 0, 0), (x, y), 160, 0)
        pygame.draw.circle(self.main_surface, (0, 0, 255), (x, y), 120, 0)
        pygame.draw.circle(self.main_surface, (255, 0, 0), (x, y), 80, 0)
        pygame.draw.circle(self.main_surface, (255, 255, 0), (x, y), 40, 0)

    # def get_score(self, x, y):

