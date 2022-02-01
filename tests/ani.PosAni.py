import pygame
import sys; sys.path.insert(0, "..")
import pgt

pygame.init()

__test_name__ = "ani.PosAni"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

image = pygame.Surface((100, 100))
image.fill(pgt.SALMON)

anchor = pgt.Element(pos=0)

e = pgt.AniElement(
    pos=(100, 100),
    anchor_element=anchor,
    size=(100, 100),
    pos_point=pgt.CC,
    image=image,
    animations=[
        pgt.ani.PosAni(
            name="move",
            frames=pgt.ani.FuncAniFrames(
                lambda p: p,
                1000
            ),
            reset_on_end=False,
            func_args=pgt.PERC,
            tot_time=1
        )
    ]
)

def change_ani_func(new_pos, func):
    pos = e.pos.copy()
    e.move.frames._func = lambda p: pos.lerp(new_pos, func(p))
    e.move.restart(e.pos)


while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == pygame.BUTTON_LEFT:
                change_ani_func(event.pos, pgt.e_out_elastic)
            elif event.button == pygame.BUTTON_RIGHT:
                change_ani_func(event.pos, pgt.e_out_exp)
            elif event.button == pygame.BUTTON_MIDDLE:
                change_ani_func(event.pos, pgt.e_out_bounce)

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    e.draw(screen)
    pygame.display.update()
