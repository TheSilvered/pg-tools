import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "draw.aa_rect"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

rect = pygame.Rect(100, 100, 150, 200)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            rect.center = event.pos

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    pgt.draw.aa_rect(screen, rect, pgt.WHITE, 50, 10, pgt.SALMON[:3] + (50,))
    pygame.display.update()
