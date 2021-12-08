import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "gui.Label"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

text = """Line 1
Line 2 l.dkfuhlefl.kasjdefhnòeiaujbnaò.kj
Line 3 a
Line 4"""


l = pgt.gui.Label(
    pos=(100, 100),
    size=(200, 115),
    text=text,
    font="consolas",
    adapt_to_width=True,
    alignment="center",
    color=pgt.SALMON,
    exceed_size=False,
    text_size=22
)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    l.draw(screen, show_rect=True)
    pygame.display.update()
