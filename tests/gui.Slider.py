import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.HSlider"
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

hruler_size = (300, 10)
hcursor_size = 20

vruler_size = (10, 300)
vcursor_size = (20, 50)

hslider = pgt.gui.HSlider(
    pos=(0, 100),
    ruler=pgt.gui.Button(
        pos=(0, 0),
        size=hruler_size,
        image=pgt.filled_surface(hruler_size, pgt.WHITE)
    ),
    cursor=pgt.gui.SliderCursor(
        pos=0,
        size=hcursor_size,
        image=pgt.filled_surface(hcursor_size, pgt.RED)
    ),
    rel_size=(0.8, None),
    min_val=-1
)

vslider = pgt.gui.VSlider(
    pos=(100, 150),
    ruler=pgt.gui.Button(
        pos=(0, 0),
        size=vruler_size,
        image=pgt.filled_surface(vruler_size, pgt.WHITE)
    ),
    cursor=pgt.gui.SliderCursor(
        pos=0,
        size=vcursor_size,
        image=pgt.filled_surface(vcursor_size, pgt.RED)
    ),
    min_val=100,
    max_val=10,
    rotation=20
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
            hslider.value = 0.5

    info.text = (hslider.value, vslider.value)

    if hslider.ruler.size != hslider.ruler.image.get_size():
        hslider.ruler.change_image(pgt.filled_surface(hslider.ruler.size, pgt.WHITE))

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    info.draw(screen)
    hslider.draw(screen)
    vslider.draw(screen)
    pygame.display.update()
