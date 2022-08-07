import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "gui.Label"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

text = """Line 1
Line 2 wordtoolongtofitinasingleline
Line 3 a
Line 4"""


l = pgt.gui.Label(
    pos=(100, 100),
    size=(200, 115),
    text=text,
    font="consolas",
    adapt_to_width=True,
    alignment=pgt.CENTER,
    color=pgt.SALMON,
    bg_color=pgt.BLACK,
    style=pgt.UNDERLINE | pgt.ITALIC,
    exceed_size=True,
    auto_size=False,
    text_size=22
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
    l.draw(screen, show_rect=True)
    pygame.display.update()
