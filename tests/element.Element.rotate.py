import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "element.Element.rotate"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()

image = pgt.load_image("test_files/image.png")

e = pgt.Element(
    pos=(100, 100),
    size=(100, 100),
    image=image,
    pos_point=pgt.Anc.CC
)

speed = 0.1

while True:
    t = clock.tick()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                speed += 0.05
            elif event.key == pygame.K_DOWN:
                speed -= 0.05

            print(f"speed: {speed:.3}")

    if pygame.key.get_pressed()[pygame.K_SPACE]:
        e.rotate(speed * t)

    screen.fill(pgt.GRAY(50))
    e.draw(screen, show_rect=True)
    pygame.display.update()
