import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "utils.change_image_ani"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

button = pgt.gui.Button(
    pos=100,
    size=(150, 70),
    normal_ani=pgt.change_image_ani(pgt.filled_surface((150, 70), pgt.RED)),
    on_hover_ani=pgt.change_image_ani(pgt.filled_surface((150, 70), pgt.GREEN)),
    on_click_ani=pgt.change_image_ani(pgt.filled_surface((150, 70), pgt.BLUE))
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
    button.draw(screen)
    pygame.display.update()
