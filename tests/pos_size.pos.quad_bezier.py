import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "pos_size.pos.quad_bezier"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

p1 = pgt.Pos(0, 0)
p2 = pgt.Pos(0, 100)
p3 = pgt.Pos(100, 100)
p4 = pgt.Pos(100, 0)
points = [p1.quad_bezier(p4, p2, p3, i / 30) for i in range(31)]


while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                p1 = pgt.Pos(pygame.mouse.get_pos())
            elif event.key == pygame.K_2:
                p2 = pgt.Pos(pygame.mouse.get_pos())
            elif event.key == pygame.K_3:
                p3 = pgt.Pos(pygame.mouse.get_pos())
            elif event.key == pygame.K_4:
                p4 = pgt.Pos(pygame.mouse.get_pos())
            else:
                continue
            points = [p1.quad_bezier(p4, p2, p3, i / 30) for i in range(31)]

    screen.fill(pgt.GRAY(50))
    for p in points:
        pgt.draw.odd_circle(screen, p, 1, pgt.WHITE)
    pgt.draw.odd_circle(screen, p1, 1, pgt.MAGENTA)
    pgt.draw.odd_circle(screen, p2, 1, pgt.YELLOW)
    pgt.draw.odd_circle(screen, p3, 1, pgt.YELLOW)
    pgt.draw.odd_circle(screen, p4, 1, pgt.MAGENTA)
    pygame.display.update()
