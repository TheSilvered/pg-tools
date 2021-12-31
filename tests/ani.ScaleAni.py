import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "ani.ScaleAni"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image = pgt.load_image("test_files/image.png")

e = pgt.AniElement(
    pos=(100, 100),
    size=(100, 100),
    pos_point=pgt.CC,
    image=image,
    animations=[
        pgt.ani.ScaleAni(
            name="resize",
            frames=pgt.ani.FuncAniFrames(
                lambda p: pgt.Size(100) + pgt.Size(100) * pgt.e_in_out_quart(p),
                1000
            ),
            reset_on_end=False,
            func_args=pgt.PERC,
            tot_time=1
        )
    ]
)

e.resize.start()

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    e.draw(screen)
    pygame.display.update()
