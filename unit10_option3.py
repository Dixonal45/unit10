# created by Allison Dixon
# last updated December 13, 2019
# unit 10 option 3: this program creates a target that lets the user click on the
# screen to get points based on how close to the center they are, and prints their points

import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 500), 0, 32)
pygame.display.set_caption("Target Game")
main_surface.fill((255, 255, 255))

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()