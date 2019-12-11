import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Pygame Demo - So Cool")
main_surface.fill((255, 255, 255))

pygame.draw.rect(main_surface, (205, 111, 215), (50, 50, 200, 100), 0)
pygame.draw.circle(main_surface, (4, 180, 200), (250, 250), 100, 35)
pygame.draw.polygon(main_surface, (80, 90, 100), ((25, 100), (100, 250),  (400, 300)), 0)
pygame.draw.line(main_surface, (103, 20, 40), (200, 200), (45, 10), 3)
pygame.draw.ellipse(main_surface, (20, 60, 90), (50, 50, 200, 100), 0)


while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
