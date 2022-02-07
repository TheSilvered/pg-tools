import pygame
import sys; sys.path.insert(0, "..")
import pgt
import random
import time
pygame.init()

__test_name__ = "particle_manager.ParticleManager"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)


def update_func(particle):
    particle[0] += particle[1]
    particle[1] += (0, 0.5)
    particle[1][0] *= 0.99
    particle[2] -= 0.3


def draw_func(particle, surface):
    rect = pygame.Rect(0, 0, round(particle[2]), round(particle[2]))
    rect.center = particle[0]
    alpha = particle[2] / 15 * 255
    pgt.draw.odd_circle(
        surface,
        particle[0],
        round(particle[2]),
        pgt.WHITE[:3] + (alpha,))
    # pygame.draw.circle(surface, pgt.WHITE, particle[0], round(particle[2]))
    # pgt.draw.aa_rect(surface, rect, pgt.WHITE[:3] + (alpha,))


def deletion_check(particle):
    return particle[2] < 1


pm = pgt.ParticleManager(draw_func, update_func, deletion_check, 1 / 60)
last_added = time.perf_counter()

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    if pygame.mouse.get_pressed(3)[0] and time.perf_counter() - last_added > 0.008:
        pm.add_particle([
            pgt.Pos(pygame.mouse.get_pos()),
            pgt.Pos(random.random() * 10 - 5, random.random() * 5 - 10),
            random.randint(10, 15)
        ])
        last_added = time.perf_counter()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    pm.draw(screen)
    pygame.display.update()
