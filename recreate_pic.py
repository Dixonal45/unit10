import pygame, sys
from pygame.locals import *
import random

pygame.init()

main_surface = pygame.display.set_mode((450, 460), 0, 32)
pygame.display.set_caption("Re-create Pygame Picture")
main_surface.fill((16, 78, 129))


def make_star():
    x = random.randint(0, 450)
    y = random.randint(0, 460)
    pygame.draw.circle(main_surface, (250, 250, 250), (x, y), 3, 0)


def make_rect(p):
    pygame.draw.rect(main_surface, (0, 0, 0), p, 0)


def make_window(e, f):
    pygame.draw.rect(main_surface, (255, 215, 0), (e, f, 10, 10), 0)


def main():
    for z in range(30):
        make_star()
    pygame.draw.circle(main_surface, (180, 180, 180), (65, 90), 40, 0)
    points = [(0, 300, 25, 180), (25, 220, 65, 300), (65, 320, 85, 190), (150, 270, 80, 300), (200, 200, 80, 300),
              (280, 390, 60, 130), (325, 340, 60, 170), (375, 220, 65, 300), (420, 300, 30, 180)]
    for p in points:
        make_rect(p)
    make_window(38, 280)
    make_window(62, 300)
    make_window(38, 405)
    make_window(62, 405)
    make_window(423, 330)
    pygame.draw.ellipse(main_surface, (120, 120, 120), (100, 220, 250, 550), 26)


main()

while True:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
