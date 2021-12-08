import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "gui.Label.auto_size"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

texts = ["a", "ab", "abc", "abcd", "abc\ndef"]
current_text = 0

l = pgt.gui.Label(
    pos=(800, 600),
    pos_point=pgt.Anc.DR,
    auto_size=True,
    text=texts[0],
    font="consolas",
    text_size=50,
    color=pgt.WHITE
)

while True:
    clock.tick()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            current_text = (current_text + 1) % len(texts)
            l.text = texts[current_text]

    screen.fill(pgt.GRAY(50))
    l.draw(screen, show_rect=True)
    pygame.display.update()
