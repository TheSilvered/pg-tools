import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "draw.even_circle"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pgt.draw.clear_cache(pgt.draw.EVEN_CIRCLE_CACHE)

    screen.fill(pgt.GRAY(50))
    pygame.draw.rect(screen, pgt.WHITE, pygame.Rect(100, 0, 200, 800))
    pgt.draw.even_circle(screen, (100, 100), 50, pgt.SALMON)
    pygame.display.update()
