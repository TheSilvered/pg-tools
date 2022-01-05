import pygame
import sys; sys.path.insert(0, "..")
import pgt
import time
pygame.init()

__test_name__ = "lang.load"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

start_time = time.perf_counter()
lang = pgt.lang.load("test_files/lang_test.lang")

label = pgt.gui.Label(
    pos=50,
    size=700,
    adapt_to_width=True,
    text=f"Time: {time.perf_counter() - start_time} s\n"
         f"set1_l1.attr1_set1_l1\n"
         f"{lang.get('set1_l1.attr1_set1_l1')}\n\n"
         f"set1_l1.set1_l2_under_set1_l1.attr1_set1_l2_under_set1_l1\n"
         f"{lang.get('set1_l1.set1_l2_under_set1_l1.attr1_set1_l2_under_set1_l1')}\n\n"
         f"set1_l1.attr2_set1_l1\n"
         f"{lang.get('set1_l1.attr2_set1_l1')}\n\n"
         f"set2_l1.attr1_set2_l1\n"
         f"{lang.get('set2_l1.attr1_set2_l1')}",
    color=pgt.WHITE,
    font="consolas"
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
    label.draw(screen)
    pygame.display.update()
