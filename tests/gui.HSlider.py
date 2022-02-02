import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.HSlider"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

hruler = pgt.gui.Button(
    pos=(0, 5),
    size=(300, 10),
    image=pgt.filled_surface((300, 10), pgt.WHITE)
)

hcursor = pgt.gui.SliderCursor(
    pos=0,
    size=20,
    image=pgt.filled_surface((20, 20), pgt.RED)
)

vruler = pgt.gui.Button(
    pos=(0, 0),
    size=(10, 300),
    image=pgt.filled_surface((10, 300), pgt.WHITE)
)

vcursor = pgt.gui.SliderCursor(
    pos=0,
    size=(10, 50),
    image=pgt.filled_surface((10, 50), pgt.RED)
)

hslider = pgt.gui.HSlider(
    pos=100,
    ruler=hruler,
    cursor=hcursor
)

vslider = pgt.gui.VSlider(
    pos=(100, 150),
    ruler=vruler,
    cursor=vcursor
)


info = pgt.gui.Label(
    pos=(0, 20),
    color=pgt.WHITE,
    text="",
    font="consolas"
)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            slider.value = 0.5

    info.text = (hslider.value, vslider.value)

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    info.draw(screen)
    hslider.draw(screen)
    vslider.draw(screen)
    pygame.display.update()
