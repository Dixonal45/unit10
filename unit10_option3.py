# created by Allison Dixon
# last updated January 6, 2020
# unit 10 option 3: this program creates a target that lets the user click on the
# screen to get points based on how close to the center they are, and prints their points

import pygame, sys
from pygame.locals import *
import target

pygame.init()
main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Target Game")
main_surface.fill((255, 255, 255))
my_target = target.Target(main_surface)
my_target.draw_target()

num_clicks = 0
while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # if the user clicks and has clicked less than five times, the computer will get the mouse coordinates
        if event.type == MOUSEBUTTONDOWN and num_clicks < 5:
            my_target.get_score(pygame.mouse.get_pos())
            num_clicks += 1
