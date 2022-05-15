import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "_test_base"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

img = pgt.draw.odd_circle(None, (0, 0), 5, pgt.MAGENTA)

a = pgt.gui.Draggable(pos=100, size=10, pos_point=pgt.CC, image=img)
b = pgt.gui.Draggable(pos=50,  size=10, pos_point=pgt.CC, image=img)

ruler = pgt.gui.Button(
    pos=(0, 0),
    size=(120, 10),
    image=pgt.filled_surface((120, 10), pgt.WHITE)
)

cursor = pgt.gui.SliderCursor(
    pos=0,
    size=(20, 10),
    image=pgt.filled_surface((20, 10), pgt.RED)
)

slider = pgt.gui.HSlider(
    pos=100,
    ruler=ruler,
    cursor=cursor
)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    slider.draw(screen)
    pgt.draw.aa_line(screen, pgt.SALMON, a.pos, b.pos, slider.value * 100 + 1)
    a.draw(screen)
    b.draw(screen)
    pygame.display.update()
