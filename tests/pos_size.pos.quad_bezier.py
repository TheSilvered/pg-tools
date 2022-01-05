import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "pos_size.pos.quad_bezier"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

p1 = pgt.gui.Draggable(pos=(0, 0),     size=11, pos_point=pgt.CC)
p2 = pgt.gui.Draggable(pos=(0, 100),   size=11, pos_point=pgt.CC)
p3 = pgt.gui.Draggable(pos=(100, 100), size=11, pos_point=pgt.CC)
p4 = pgt.gui.Draggable(pos=(100, 0),   size=11, pos_point=pgt.CC)
points = [p1.pos.quad_bezier(p4.pos, p2.pos, p3.pos, i / 100) for i in range(101)]


while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    p1.update()
    p2.update()
    p3.update()
    p4.update()

    if p1.dragging or p2.dragging or p3.dragging or p4.dragging:
        points = [p1.pos.quad_bezier(p4.pos, p2.pos, p3.pos, i / 100) for i in range(101)]

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    for p in points:
        pgt.draw.odd_circle(screen, p, 1, pgt.WHITE)
    pgt.draw.odd_circle(screen, p1.pos, 5, pgt.MAGENTA)
    pgt.draw.odd_circle(screen, p2.pos, 5, pgt.YELLOW)
    pgt.draw.odd_circle(screen, p3.pos, 5, pgt.YELLOW)
    pgt.draw.odd_circle(screen, p4.pos, 5, pgt.MAGENTA)
    pygame.display.update()
