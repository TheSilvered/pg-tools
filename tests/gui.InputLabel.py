import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "gui.InputLabel"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

def print_self(label):
    print(label.text)

input_label = pgt.gui.InputLabel(
    pos=100,
    size=(500, 30),
    image=pgt.filled_surface((500, 30), pgt.GRAY(80)),
    # right_aligned=True,
    char_subs={"\t": "     "},
    func=print_self,
    func_as_method=True,
    caret_color=pgt.WHITE,
    text_label=pgt.gui.Label(
        font="calibri",
        text_size=24,
        size=(494, 24),
        pos_point=pgt.CC,
        anchor_point=pgt.CC,
        color=pgt.WHITE
    )
)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        input_label.handle_event(event)

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    input_label.draw(screen)
    input_label.auto_run()
    pygame.display.update()
