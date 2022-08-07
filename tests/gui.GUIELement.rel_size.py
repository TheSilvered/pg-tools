import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "gui.GUIELement.rel_size"
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

def on_size_change(e):
    e.image = pgt.filled_surface(e.size, pgt.SALMON)

e = pgt.gui.GUIElement(
    rel_size=(0.5, -50),
    on_size_change=on_size_change
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
    e.draw(screen)
    pygame.display.update()
