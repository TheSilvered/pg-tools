import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "mathf.e_in_out"
screen = pygame.display.set_mode((800, 700))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

functions = [
    pgt.e_in_sin,     pgt.e_out_sin,     pgt.e_in_out_sin,
    pgt.e_in_quad,    pgt.e_out_quad,    pgt.e_in_out_quad,
    pgt.e_in_cubic,   pgt.e_out_cubic,   pgt.e_in_out_cubic,
    pgt.e_in_quart,   pgt.e_out_quart,   pgt.e_in_out_quart,
    pgt.e_in_quint,   pgt.e_out_quint,   pgt.e_in_out_quint,
    pgt.e_in_exp,     pgt.e_out_exp,     pgt.e_in_out_exp,
    pgt.e_in_circ,    pgt.e_out_circ,    pgt.e_in_out_circ,
    pgt.e_in_back,    pgt.e_out_back,    pgt.e_in_out_back,
    pgt.e_in_elastic, pgt.e_out_elastic, pgt.e_in_out_elastic,
    pgt.e_in_bounce,  pgt.e_out_bounce,  pgt.e_in_out_bounce
]

points = []
precision = 100


def calc_points(prec):
    global points
    prec = pgt.clamp(prec, 1, 200)
    points = []
    for func_idx, func in enumerate(functions):
        points.append([])
        for i in range(prec, -1, -1):
            x = 100 * ((prec - i) / prec) + func_idx % 6 * 130 + 25
            y = int(func(i / prec) * 100) + func_idx // 6 * 130 + 25
            points[-1].append((x, y))

calc_points(200)
actual_points = points.copy()
calc_points(precision)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEWHEEL:
            precision += event.y
            precision = pgt.clamp(precision, 1, 200)
            calc_points(precision)
            print(precision)

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    for i in actual_points:
        pygame.draw.lines(screen, pgt.MAGENTA, False, i, 3)

    for i in points:
        pygame.draw.lines(screen, pgt.SALMON, False, i, 3)

    pygame.display.update()
