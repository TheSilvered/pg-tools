import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.Font"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

chars_info = pgt.parse_json_file("test_files/font_info.json")
image = pgt.load_image("test_files/font_image.png")

font = pgt.gui.Font(image, size=44, **chars_info)

l1 = pgt.gui.Label(
    pos=(400, 100),
    auto_size=True,
    pos_point=pgt.CC,
    text="Hi, my name is TheSilvered and I'm 15.\nUnknown chars: <>àèéìùòùç",
    font=font,
    color=pgt.LIGHT_BLUE,
    # style="no_aa",
    # bg_color=pgt.GRAY(50)
)

l2 = pgt.gui.Label(
    pos=(400, 400),
    auto_size=True,
    pos_point=pgt.CC,
    text="Hi, my name is TheSilvered and I'm 15.\nUnknown chars: <>àèéìùòùç",
    font=font,
    color=pgt.RED,
    # style="no_aa",
    # bg_color=pgt.GRAY(50)
)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    l1.draw(screen)
    l2.draw(screen)
    pygame.display.update()
