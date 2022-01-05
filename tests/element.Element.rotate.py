import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "element.Element.rotate"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)

image = pgt.load_image("test_files/image.png", True)

e = pgt.Element(
    pos=(100, 100),
    size=(100, 100),
    image=image,
    pos_point=pgt.CC,
    img_offset=-1  # To keep the edges smooth, the image
)                  # has a transparent line on each side

speed = 0.1

while True:
    t = clock.tick()
    fps.text = int(clock.get_fps())

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
    fps.draw(screen)
    e.draw(screen, show_rect=True)
    pygame.display.update()
