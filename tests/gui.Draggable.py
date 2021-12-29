import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.Draggable"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image = pgt.load_image("test_files/image.png", True)

e = pgt.gui.Draggable(
    pos=(100, 100),
    size=(100, 100),
    image=image,
    pos_point=pgt.Anc.CC,
    img_offset=-1,
    boundary_top=0,
    boundary_left=100,
    boundary_right=500,
    boundary_bottom=500,
    locked=False
)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    e.draw(screen)
    pygame.draw.rect(screen, pgt.MAGENTA, pygame.Rect(100, 100, 400, 400), 1)
    pygame.display.update()
