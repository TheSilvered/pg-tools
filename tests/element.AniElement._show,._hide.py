import pygame
import sys; sys.path.insert(0, "..")
import pgt
pygame.init()

__test_name__ = "element.AniElement._show,._hide"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption(__test_name__)
clock = pygame.time.Clock()
fps = pgt.gui.Label(pos=0, font="consolas", text_size=20, color=pgt.WHITE)
hidden = pgt.gui.Label(
    pos=(0, 20),
    font="consolas",
    text_size=20,
    color=pgt.WHITE
)

image = pygame.Surface((100, 100), flags=pygame.SRCALPHA)
image.fill(pgt.SALMON)


class AlphaAni(pgt.ani.AniBase):
    def start(self, *args, **kwargs):
        super().start(*args, **kwargs)
        self.element_val = self.e.alpha

    def set_element(self):
        self.e.alpha = pgt.clamp(self.get_frame(), 0, 1) * 255

    def reset_element(self):
        self.e.alpha = self.element_val


e = pgt.AniElement(
    pos=(100, 100),
    size=(100, 100),
    image=image,
    offset=(10, 10),
    animations=[
        AlphaAni(
            name="_show",
            frames=pgt.ani.FuncAniFrames(
                lambda p: pgt.e_in_sin(p),
                60
            ),
            tot_time=0.5,
            func_args=pgt.PERC,
            reset_on_end=False
        ),
        AlphaAni(
            name="_hide",
            frames=pgt.ani.FuncAniFrames(
                lambda p: (pgt.e_in_sin(p) - 1) * -1,
                60
            ),
            tot_time=0.5,
            func_args=pgt.PERC,
            reset_on_end=False
        )
    ]
)

while True:
    clock.tick()
    fps.text = int(clock.get_fps())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if e.hidden: e.show()
                else: e.hide()

    hidden.text = f"hidden: {e.hidden}"

    screen.fill(pgt.GRAY(50))
    fps.draw(screen)
    e.draw(screen)
    hidden.draw(screen)
    pygame.display.update()
