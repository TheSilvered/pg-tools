import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "utils.trasform_func"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

e_size = (200, 200)

e = pgt.gui.SurfaceElement(
    pos=250,
    size=e_size,
    bg_color=pgt.GRAY(70),
    rotation=60
)

func = pgt.transform_func(e)

expected_rect = pygame.Rect((0, 0), e_size)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    e.draw(screen, show_rect=True)
    pygame.draw.rect(screen, pgt.GRAY(70), expected_rect)
    pgt.draw.odd_circle(screen, func(pygame.mouse.get_pos()), 1, pgt.MAGENTA)
    pygame.display.update()
