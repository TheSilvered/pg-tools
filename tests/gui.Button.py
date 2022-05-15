import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "gui.Button"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

image = pgt.load_image("test_files/image.png")
font_image = pgt.load_image("test_files/font_image.png")
font_info = pgt.parse_json_file("test_files/font_info.json")

b = pgt.gui.Button(
    pos=(400, 300),
    size=(100, 100),
    pos_point=pgt.CC,
    image=image,
    text_label=pgt.gui.Label(
        pos=(0, 0),
        pos_point=pgt.CC,
        anchor_point=pgt.CC,
        auto_size=True,
        text="print('Hello')",
        font=pgt.gui.Font(font_image, **font_info, size=22),
        color=pgt.RED,
        alignment=pgt.CENTER
    ),
    func=print,
    func_args=["Hello"],
    normal_ani=pgt.ani.ScaleAni(
        frames=pgt.ani.FuncAniFrames(
            lambda p, a: a.element_val + (pgt.Size(100) - a.element_val) * pgt.e_out_exp(p),
            1000
        ),
        reset_on_end=False,
        func_args=pgt.PERC | pgt.ANIMATION,
        tot_time=.2,
        smooth=True
    ),
    on_hover_ani=pgt.ani.ScaleAni(
        frames=pgt.ani.FuncAniFrames(
            lambda p, a: a.element_val + (pgt.Size(115) - a.element_val) * pgt.e_out_exp(p),
            1000
        ),
        reset_on_end=False,
        func_args=pgt.PERC | pgt.ANIMATION,
        tot_time=.3,
        smooth=True
    ),
    on_click_ani=pgt.ani.ScaleAni(
        frames=pgt.ani.FuncAniFrames(
            lambda p, a: a.element_val + (pgt.Size(80) - a.element_val) * pgt.e_out_exp(p),
            1000
        ),
        reset_on_end=False,
        func_args=pgt.PERC | pgt.ANIMATION,
        tot_time=.1,
        smooth=True
    )
)

info = pgt.gui.Label(
    pos=(0, 20),
    color=pgt.WHITE,
    text="",
    font="consolas"
)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    info.text = b.current_ani
    b.auto_run()

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    b.draw(screen, show_rect=True)
    info.draw(screen)
    pygame.display.update()
