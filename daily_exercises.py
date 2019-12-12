import pygame, sys
from pygame.locals import *

pygame.init()

main_surface = pygame.display.set_mode((500, 400), 0, 32)
pygame.display.set_caption("Pygame Daily Exercises")
main_surface.fill((255, 255, 255))

pygame.draw.circle(main_surface, (0, 0, 255), (350, 50), 20, 0)
pygame.draw.polygon(main_surface, (10, 250, 10), ((25, 120), (90, 270),  (250, 270), (305, 120), (165, 10)), 0)
pygame.draw.rect(main_surface, (255, 0, 0), (250, 150, 100, 50), 0)
pygame.draw.line(main_surface, (0, 0, 255), (70, 80), (130, 80), 4)
pygame.draw.line(main_surface, (0, 0, 255), (70, 135), (130, 135), 4)
pygame.draw.line(main_surface, (0, 0, 255), (70, 135), (130, 80), 2)
pygame.draw.ellipse(main_surface, (255, 0, 0), (350, 250, 50, 90), 2)

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
