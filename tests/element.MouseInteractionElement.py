import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "element.MouseInteractionElement"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image = pygame.Surface((100, 100))
image.fill(pgt.SALMON)

e = pgt.MouseInteractionElement(
    pos=(100, 100),
    size=(100, 100),
    image=image,
    pos_point=pgt.Anc.CC
)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    e.draw(screen)
    print(e.hovered, e.clicked)
    pygame.display.update()
