import pygame
import sys; sys.path.insert(0, "..")
import tools_for_pygame as pgt
pygame.init()

__test_name__ = "label.Label.text"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

texts = ["Text 1:\ntest 1", "Text 2:\ntest 2", "Text 3:\ntest 3"]

current_text = 0

l = pgt.gui.Label(
    pos=(100, 100),
    text=texts[0],
    text_size=140,
    alpha=50,
    auto_size=True,
    rotation=45
)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_text = (current_text + 1) % len(texts)
            l.text = texts[current_text]
            # l.rotate(10)

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    l.draw(screen, show_rect=True)
    pygame.display.update()
