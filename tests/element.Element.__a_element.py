import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "element.Element.__a_element"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image1 = pygame.Surface((100, 100), flags=pygame.SRCALPHA)
image1.fill(pgt.SALMON)

image2 = pygame.Surface((100, 100))
image2.fill(pgt.EMERALD)

e1 = pgt.Element(
    pos=(100, 100),
    size=(100, 100),
    image=image1,
    pos_point=pgt.Anc.CC
)

e2 = pgt.Element(
    anchor_element=e1,
    anchor_point=pgt.Anc.CC,
    size=(100, 100),
    image=image2,
    alpha=127
)

# e1.rotate(45)
# e2.rotate(45)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            e1.cc = event.pos

    screen.fill(pgt.GRAY(50))
    e1.draw(screen, flags=pygame.BLEND_ADD)
    e2.draw(screen)
    pygame.display.update()
