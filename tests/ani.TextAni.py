import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "animations.TextAni"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

animation_texts = ["Frame 1", "\nFrame 2", "Frame 3"]

l = pgt.gui.AniLabel(
    pos=(100, 100),
    size=(100, 100),
    text="Starting Text",
    font="consolas",
    adapt_to_width=True,
    auto_size=False,
    alignment=pgt.CENTER,
    color=pgt.WHITE,
    text_size=22,
    animations=[
        pgt.ani.TextAni(
            name="text_ani",
            frames=animation_texts,
            reset_on_end=True,
            time=1
        )
    ]
)

l.text_ani.start()

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    l.draw(screen)
    pygame.display.update()
