import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "pos_size.pos.slerp"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

offset = 0

pos1 = pgt.Pos(100, 100)
pos2 = pgt.Pos(10, 0)
c = pgt.Pos(0)
points = [pos1.slerp(pos2, i / 100, 200) for i in range(0, 101)]

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                pos1 = pgt.Pos(event.pos)
                points = [pos1.slerp(pos2, i / 30, c) for i in range(0, 31)]
            elif event.button == pygame.BUTTON_RIGHT:
                pos2 = pgt.Pos(event.pos)
                points = [pos1.slerp(pos2, i / 30, c) for i in range(0, 31)]
            elif event.button == pygame.BUTTON_MIDDLE:
                c = pgt.Pos(event.pos)
                points = [pos1.slerp(pos2, i / 30, c) for i in range(0, 31)]

    screen.fill(pgt.GRAY(50))
    for i, p in enumerate(points):
        col = pgt.GRAY(255 * (i / len(points)))
        pgt.draw.odd_circle(screen, p + offset, 1, col)
    pgt.draw.odd_circle(screen, pos1 + offset, 1, pgt.MAGENTA)
    pgt.draw.odd_circle(screen, pos2 + offset, 1, pgt.MAGENTA)
    pgt.draw.odd_circle(screen, c + offset, 1, pgt.YELLOW)
    pygame.display.update()
