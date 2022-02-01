import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "animations.TextureAni"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

t1 = pgt.filled_surface((100, 100), pgt.RED)
t2 = pgt.filled_surface((100, 100), pgt.GREEN)
t3 = pgt.filled_surface((100, 100), pgt.BLUE)

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
            loop=False,
            queued_ani=pgt.ani.TextureAni(
                    name="queued_flash",
                    frames=[t1, t2, t3],
                    time=1
                )
        )
    ],
    rotation=45,
    alpha=152
)

e.flash.start()

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
