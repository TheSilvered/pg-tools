import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "_test_base"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    pygame.display.update()
