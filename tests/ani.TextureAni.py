import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "animations.TextureAni"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

t1 = pygame.Surface((100, 100))
t2 = pygame.Surface((100, 100))
t3 = pygame.Surface((100, 100))
t1.fill(pgt.RED)
t2.fill(pgt.GREEN)
t3.fill(pgt.BLUE)

base = pygame.Surface((100, 100))
base.fill(pgt.SALMON)

e = pgt.AniElement(
    pos=(100, 100),
    size=(100, 100),
    image=base,
    animations=[
        pgt.ani.TextureAni(
            name="flash",
            frames=[t1, t2, t3],
            time=.5,
            loop=False
        )
    ],
    rotation=45,
    alpha=152
)

e.flash.start()

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    e.draw(screen)
    # print(e.image.get_at((0, 0)))
    pygame.display.update()
