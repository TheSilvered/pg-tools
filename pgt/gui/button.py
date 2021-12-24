from pgt.element import MouseInteractionAniElement, Anc
from pgt.ani import AniBase
from .label import Label
import pygame.mixer
from typing import Optional, Callable, Iterable
from pgt.constants import BUTTON_NORMAL, BUTTON_CLICK, BUTTON_HOVER


class Button(MouseInteractionAniElement):
    """
    Button(MouseInteractionAniElement)

    Type: class

    Description: a customizable button that can run a function
        when clicked

    Args:
        'normal_ani' (AniBase?): animation that plays when the button
            is idle
        'on_hover_ani' (AniBase?): animation that plays when the
            button is hovered by the cursor
        'on_click_ani' (AniBase?): animation that plays when the
            button is clicked
        'repeat_normal_ani' (bool): if the animation should be
            started each frame or only once
        'repeat_hover_ani' (bool): if the animation should be
            started each frame or only once
        'repeat_click_ani' (bool): if the animation should be
            started each frame or only once
        'text_label' (Label?): a Label that gets drawn in front of
            the button
        'text_label_point' (Anc): element_point of the label
        'func' (Callable): function to run when the button is pressed
        'func_args' (Iterable?): *args of the function
        'func_kwargs' (dict?): **kwargs of the function
        'button' (int): which mouse button should activate the button
            1 - left, 2 - middle, 3 - right
        'sound' (pygame.mixer.Sound?): a sound to play when the
            button is clicked

    Attrs:
        'normal_ani' (AniBase?): see 'normal_ani' in args
        'on_hover_ani' (AniBase?): see 'on_hover_ani' in args
        'on_click_ani' (AniBase?): see 'on_click_ani' in args
        'repeat_normal_ani' (bool): see 'repeat_normal_ani' in args
        'repeat_hover_ani' (bool): see 'repeat_hover_ani' in args
        'repeat_hover_ani' (bool): see 'repeat_hover_ani' in args
        'func' (Callable?): see 'func' in args
        'fargs' (Iterable?): see 'func_args' in args
        'fkwargs' (dict?): see 'func_kwargs' in args
        'button' (int): see 'button' in args
        'sound' (pygame.mixer.Sound?): see 'sound' in args
        'force_state' (int?): which state is shown of the button,
            if set to None the current one is shown.
            The module provides three constants BUTTON_NORMAL,
            BUTTON_HOVER and BUTTON_CLICK
        'label' (Label?): see 'label' in args

    Properties:
        'button_clicked' (bool, readonly): if the button is clicked
            with the assigned mouse button

    Methods:
        'run()': runs the function
        'auto_run()': to call every frame, calls 'run' automatically
            when the button is pressed and plays the sound
    """
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
       sound: Optional[pygame.mixer.Sound] = None,
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
