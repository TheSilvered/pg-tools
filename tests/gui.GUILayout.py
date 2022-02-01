import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.GUILayout"
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

lyt = pgt.gui.GUILayout({
    "hi_button": pgt.gui.Button(
        pos=0,
        size=(80, 40),
        pos_point=pgt.CC,
        anchor_point=pgt.CC,
        image=pgt.filled_surface((80, 40), pgt.R(50)),
        func=print,
        func_args=["Hi :)"],
        text_label=pgt.gui.Label(
            pos=0,
            pos_point=pgt.CC,
            anchor_point=pgt.CC,
            font="consolas",
            text_size=20,
            text="Hi",
            auto_size=True,
            color=pgt.WHITE
        ),
        hint_bg=pgt.Element(
            pos=0,
            size=(150, 40),
            image=pgt.filled_surface((150, 40), pgt.G(50))
        ),
        hint_label=pgt.gui.Label(
            pos=0,
            pos_point=pgt.CC,
            anchor_point=pgt.CC,
            font="consolas",
            text_size=20,
            text="Prints 'Hi'",
            auto_size=True,
            color=pgt.WHITE
        )
    ),
    "other_button": pgt.gui.Button(
        pos=0,
        size=(80, 40),
        pos_point=pgt.DR,
        anchor_point=pgt.DR,
        image=pgt.filled_surface((80, 40), pgt.R(100)),
        func=print,
        func_args=["Hi2 :)"],
        text_label=pgt.gui.Label(
            pos=0,
            pos_point=pgt.CC,
            anchor_point=pgt.CC,
            font="consolas",
            text_size=20,
            text="Hi2",
            auto_size=True,
            color=pgt.WHITE
        ),
        hint_bg=pgt.Element(
            pos=0,
            size=(150, 40),
            image=pgt.filled_surface((150, 40), pgt.G(100))
        ),
        hint_label=pgt.gui.Label(
            pos=0,
            pos_point=pgt.CC,
            anchor_point=pgt.CC,
            font="consolas",
            text_size=20,
            text="Prints 'Hi2'",
            auto_size=True,
            color=pgt.WHITE
        )
    ),
    "layout_in_layout": pgt.gui.GUILayout(
        {
            "hi_button": pgt.gui.Button(
                pos=0,
                size=(80, 40),
                pos_point=pgt.CC,
                anchor_point=pgt.CC,
                image=pgt.filled_surface((80, 40), pgt.B(50)),
                func=print,
                func_args=["Hii :)"],
                text_label=pgt.gui.Label(
                    pos=0,
                    pos_point=pgt.CC,
                    anchor_point=pgt.CC,
                    font="consolas",
                    text_size=20,
                    text="Hii",
                    auto_size=True,
                    color=pgt.WHITE
                ),
                hint_bg=pgt.Element(
                    pos=0,
                    size=(150, 40),
                    image=pgt.filled_surface((150, 40), pgt.B(50))
                ),
                hint_label=pgt.gui.Label(
                    pos=0,
                    pos_point=pgt.CC,
                    anchor_point=pgt.CC,
                    font="consolas",
                    text_size=20,
                    text="Prints 'Hii'",
                    auto_size=True,
                    color=pgt.WHITE
                )
            ),
            "other_button": pgt.gui.Button(
                pos=0,
                size=(80, 40),
                pos_point=pgt.DR,
                anchor_point=pgt.DR,
                image=pgt.filled_surface((80, 40), pgt.B(100)),
                func=print,
                func_args=["Hii2 :)"],
                text_label=pgt.gui.Label(
                    pos=0,
                    pos_point=pgt.CC,
                    anchor_point=pgt.CC,
                    font="consolas",
                    text_size=20,
                    text="Hii2",
                    auto_size=True,
                    color=pgt.WHITE
                ),
                hint_bg=pgt.Element(
                    pos=0,
                    size=(150, 40),
                    image=pgt.filled_surface((150, 40), pgt.B(100))
                ),
                hint_label=pgt.gui.Label(
                    pos=0,
                    pos_point=pgt.CC,
                    anchor_point=pgt.CC,
                    font="consolas",
                    text_size=20,
                    text="Prints 'Hii2'",
                    auto_size=True,
                    color=pgt.WHITE
                )
            )
        },
        ["hi_button", "other_button"],
        pos=0,
        size=(200, 150),
        pos_point=pgt.DL,
        anchor_point=pgt.DL,
        bg_color=pgt.WHITE
    )

}, ["hi_button", "other_button", "layout_in_layout"], pos=0, size=(800, 600))

while True:
    clock.tick()
    try:
        fps.text = int(clock.get_fps())
    except OverflowError:
        fps.text = "inf"

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.WINDOWRESIZED:
            lyt.size = (event.x, event.y)

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    lyt.draw(screen)
    pygame.display.update()
