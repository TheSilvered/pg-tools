import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "gui.Draggable"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

image = pgt.load_image("test_files/image.png", True)

e = pgt.gui.Draggable(
    pos=(100, 100),
    size=(100, 100),
    image=image,
    pos_point=pgt.CC,
    img_offset=-1,
    boundary_top=100,
    boundary_left=100,
    boundary_right=500,
    boundary_bottom=500,
    locked=False,
    snap_pos=200,
    animations=[
        pgt.ani.PosAni(
            name="_snap",
            frames=pgt.ani.FuncAniFrames(
                lambda p, a, e: a.element_val.lerp(e.snap_pos, pgt.e_out_elastic(p)),
                60
            ),
            func_args=pgt.PERC | pgt.ANIMATION | pgt.ELEMENT,
            tot_time=0.8,
            reset_on_end=False
        )
    ]
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
    pygame.draw.rect(screen, pgt.MAGENTA, pygame.Rect(100, 100, 400, 400), 1)
    pygame.display.update()
