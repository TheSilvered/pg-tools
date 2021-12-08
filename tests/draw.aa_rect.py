import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "draw.aa_rect"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

rect = pygame.Rect(100, 100, 100, 40)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            rect.center = event.pos

    screen.fill(pgt.GRAY(50))
    pgt.draw.aa_rect(screen, rect, pgt.WHITE, 3, pgt.SALMON, 2)
    pygame.display.update()
