import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "element.Element.draw"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image1 = pygame.Surface((100, 100))
image1.fill(pgt.SALMON)

image2 = pygame.Surface((100, 100))
image2.fill(pgt.EMERALD)

e1 = pgt.Element(
    pos=(100, 100),
    size=(100, 100),
    image=image1,
    pos_point=pgt.CC,
    offset=(10, 10)
)

e2 = pgt.Element(
    pos=(100, 100),
    size=(100, 100),
    image=image2
)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    e1.draw(screen, flags=pygame.BLEND_ADD)
    e2.draw(screen, flags=pygame.BLEND_SUB)
    pygame.display.update()
