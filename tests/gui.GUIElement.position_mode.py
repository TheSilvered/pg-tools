import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "gui.GUIElement.position_mode"
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

button_image1 = pgt.draw.aa_rect(
    None,
    pygame.Rect(0, 0, 150, 40),
    pgt.WHITE,
    5,
    2,
    pgt.GRAY(130)
)

button_image2 = pgt.draw.aa_rect(
    None,
    pygame.Rect(0, 0, 200, 80),
    pgt.WHITE,
    5,
    2,
    pgt.GRAY(130)
)

button_image3 = pgt.draw.aa_rect(
    None,
    pygame.Rect(0, 0, 100, 50),
    pgt.WHITE,
    5,
    2,
    pgt.GRAY(130)
)

button1 = pgt.gui.Button(
    pos=0,
    image=button_image1,
    size=(150, 40),
    position_mode=pgt.AUTOMATIC,
    padding_top=50,
    text_label=pgt.gui.Label(
        pos=0,
        font="consolas",
        text="Hello World!",
        auto_size=True,
        alignment=pgt.CENTER,
        pos_point=pgt.CC,
        anchor_point=pgt.CC,
        offset=(-2, 3)
    ),
    func=print,
    func_args=["Hello World!"]
)

button2 = pgt.gui.Button(
    pos=0,
    image=button_image2,
    size=(200, 80),
    position_mode=pgt.AUTOMATIC,
    text_label=pgt.gui.Label(
        pos=0,
        font="consolas",
        text="Really big\nHello World!",
        auto_size=True,
        alignment=pgt.CENTER,
        pos_point=pgt.CC,
        anchor_point=pgt.CC,
        offset=(-2, 3)
    ),
    func=print,
    func_args=["Big Hello World!"]
)

button3 = pgt.gui.Button(
    pos=0,
    image=button_image3,
    size=(100, 50),
    padding_bottom=30,
    position_mode=pgt.AUTOMATIC,
    text_label=pgt.gui.Label(
        pos=0,
        font="consolas",
        text="Hello!",
        auto_size=True,
        alignment=pgt.CENTER,
        pos_point=pgt.CC,
        anchor_point=pgt.CC,
        offset=(-2, 3)
    ),
    func=print,
    func_args=["Tiny Hello World!"]
)

layout = pgt.gui.GUILayout(
    pos=pgt.Pos(100),
    size=(90, 400),
    rel_size=(0.5, None),
    bg_color=pgt.GRAY(60),
    adapt_height=True,
    elements={
        "button1": button1,
        "button2": button2,
        "button3": button3
    }
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
    layout.draw(screen)
    pygame.display.update()
