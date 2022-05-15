import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "pos_size.pos.slerp"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

a = pgt.gui.Draggable(pos=100, size=10, pos_point=pgt.CC)
b = pgt.gui.Draggable(pos=50,  size=10, pos_point=pgt.CC)
c = pgt.gui.Draggable(pos=0,   size=10, pos_point=pgt.CC)

points = [a.pos.slerp(b.pos, i / 100, 200) for i in range(0, 101)]

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    a.update()
    b.update()
    c.update()

    if a.dragging or b.dragging or c.dragging:
        points = [a.pos.slerp(b.pos, i / 100, c.pos) for i in range(0, 101)]

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    for i, p in enumerate(points):
        col = pgt.G(255 * (i / len(points)))
        pgt.draw.odd_circle(screen, p, 1, col)
    pgt.draw.odd_circle(screen, a.pos, 5, pgt.MAGENTA)
    pgt.draw.odd_circle(screen, b.pos, 5, pgt.MAGENTA)
    pgt.draw.odd_circle(screen, c.pos, 5, pgt.YELLOW)
    pygame.display.update()
