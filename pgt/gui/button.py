from pgt.element import MouseInteractionAniElement, Anc
from pgt.ani import AniBase
from .label import Label
import pygame.mixer
from typing import Optional, Callable, Iterable

BUTTON_NORMAL = 1
BUTTON_HOVER = 2
BUTTON_CLICK = 3


class Button(MouseInteractionAniElement):
    def __init__(self,
       normal_ani: Optional[AniBase] = None,
       on_hover_ani: Optional[AniBase] = None,
       on_click_ani: Optional[AniBase] = None,
       repeat_normal_ani: bool = False,
       repeat_hover_ani: bool = False,
       repeat_click_ani: bool = False,
       text_label: Optional[Label] = None,
       text_label_point: str = Anc.CC,
       func: Optional[Callable] = None,
       func_args: Optional[Iterable] = None,
       func_kwargs: Optional[dict] = None,
       button: int = 0,
       sound: pygame.mixer.Sound = None,
       *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Animation setup
        if normal_ani is not None:
            normal_ani.name = "normal_ani"
            normal_ani.id = -1
            self.add_ani(normal_ani)
        else: self.normal_ani = None

        if on_hover_ani is not None:
            on_hover_ani.name = "on_hover_ani"
            on_hover_ani.id = -1
            self.add_ani(on_hover_ani)
        else: self.on_hover_ani = None

        if on_click_ani is not None:
            on_click_ani.name = "on_click_ani"
            on_click_ani.id = -1
            self.add_ani(on_click_ani)
        else: self.on_click_ani = None

        self.repeat_normal_ani = repeat_normal_ani
        self.repeat_hover_ani = repeat_hover_ani
        self.repeat_click_ani = repeat_click_ani

        self.__started_ani = None

        # Function setup
        self.func = func
        if func_args is None: func_args = []
        self.fargs = func_args
        if func_kwargs is None: func_kwargs = {}
        self.fkwargs = func_kwargs

        # Other
        self.button = button
        self.sound = sound

        self.__pressed = False
        self.force_state = None

        # Label setup
        self.label = text_label
        if not self.label: return

        self.label._Element__a_element = self
        self.label._a_point = text_label_point

    @property
    def button_clicked(self):
        return self.clicked[self.button]

    def run(self) -> None:
        if self.func: self.func(*self.fargs, **self.fkwargs)

    def auto_run(self) -> bool:
        if self.button_clicked:
            if not self.__pressed and self.sound is not None:
                pygame.mixer.Sound.play(self.sound)
            self.__pressed = True
        elif self.hovered:
            if self.__pressed:
                self.run()
                self.__pressed = False
                return True
        else:
            self.__pressed = False

        return False

    def draw(self, *args, **kwargs) -> None:
        hovered = self.hovered
        clicked = self.button_clicked

        if self.force_state:
            if self.force_state == BUTTON_NORMAL:
                hovered = clicked = False
            elif self.force_state == BUTTON_HOVER:
                hovered = True
                clicked = False
            elif self.force_state == BUTTON_CLICK:
                clicked = True

        if clicked and self.on_click_ani is not None:
            if not self.__started_ani == "c" or self.repeat_click_ani:
                self.on_click_ani.start()
                self.__started_ani = "c"

        elif hovered and self.on_hover_ani is not None:
            if not self.__started_ani == "h" or self.repeat_hover_ani:
                self.on_hover_ani.start()
                self.__started_ani = "h"

        elif self.normal_ani is not None:
            if not self.__started_ani == "n" or self.repeat_normal_ani:
                self.normal_ani.start()
                self.__started_ani = "n"

        if self.hidden: return

        super().draw(*args, **kwargs)
        if self.label:
            self.label.draw(*args, **kwargs)
