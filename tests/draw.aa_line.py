import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "_test_base"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

line_y = 10
line_ascending = True

while True:
    clock.tick(100)
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if line_ascending:
        line_y += 1
    else:
        line_y -= 1

    if line_y > 399:
        line_ascending = False
    elif line_y < 10:
        line_ascending = True

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    pgt.draw.aa_line(screen, pgt.SALMON, (100, line_y), (400, 400), 10)
    pygame.display.update()
