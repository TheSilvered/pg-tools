import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.SurfaceElement"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image1 = pygame.Surface((100, 100))
image1.fill(pgt.SALMON)

image2 = pygame.Surface((100, 100))
image2.fill(pgt.EMERALD)

t1 = pygame.Surface((100, 100))
t2 = pygame.Surface((100, 100))
t3 = pygame.Surface((100, 100))
t1.fill(pgt.RED)
t2.fill(pgt.GREEN)
t3.fill(pgt.BLUE)

e1 = pgt.AniElement(
    pos=(100, 100),
    size=(100, 100),
    image=image1,
    pos_point=pgt.Anc.CC,
    animations=[
        pgt.ani.TextureAni(
            name="flash",
            frames=[t1, t2, t3],
            time=1,
            loop=False
        )
    ]
)

e2 = pgt.Element(
    pos=(100, 100),
    size=(100, 100),
    image=image2
)

s_e = pgt.gui.SurfaceElement(
    pos=(200, 200),
    size=(250, 250),
    pos_point=pgt.Anc.CC,
    elements=[e1, e2],
    bg_color=pgt.GRAY(50),
    alpha=127,
    rotation=30
)

e1.flash.start()

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                s_e.rotate(10)

    s_e.pos = pygame.mouse.get_pos()

    screen.fill(pgt.GRAY(50))
    s_e.draw(screen, elements_args=[{}, {"flags": pygame.BLEND_SUB}], show_rect=True)
    pygame.display.update()
