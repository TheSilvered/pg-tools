from typing import Iterable, Any
from pgt.type_hints import _col_type
import pygame
from pgt.element import Element, AniElement


class SurfaceElement(Element):
    def __init__(self,
                 elements: Iterable = None,
                 bg_color: _col_type = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        if elements is None: elements = []
        self.__elements = elements

        self.image = pygame.Surface(self.size)
        self.image.set_alpha(self._alpha)
        if self._Element__backup_image is not None:
            self._Element__backup_image = self.image.copy()
        self.image = pygame.transform.rotate(self.image, self._rot)

        if bg_color is None: bg_color = (0, 0, 0)
        self.bg_color = bg_color

        self.__current_index = 0
        self.__tot_len = len(self.__elements)
        self.__size = self.rect.size

    def __getitem__(self, index):
        return self.__elements[index]

    def __setitem__(self, index, value):
        self.__elements[index] = value

    def __delitem__(self, index):
        del self.__elements[index]

    def __len__(self):
        return self.__tot_len

    def __iter__(self):
        return self

    def __next__(self):
        self.__current_index += 1
        if self.__current_index - 1 == self.__tot_len:
            self.__current_index = 0
            raise StopIteration

        return self[self.__current_index - 1]

    @property
    def elements(self):
        return self.__elements

    @elements.setter
    def elements(self, value):
        self.__tot_len = len(value)
        self.__elements = value

    def append(self, element) -> None:
        self.__elements.append(element)
        self.__tot_len += 1

    def remove(self, element, key=lambda a, b: a == b) -> None:
        for i, e in enumerate(self.__elements):
            if key(element, e):
                del self.__elements[i]
                self.__tot_len -= 1
                return

    def index(self, element, key=lambda a, b: a == b) -> Any:
        for i, e in enumerate(self.__elements):
            if key(element, e):
                return i

    def insert(self, index, element) -> None:
        self.__elements.insert(index, element)
        self.__tot_len += 1

    def clear(self) -> None:
        self.__elements.clear()
        self.__tot_len = 0

    def pop(self) -> Any:
        i = self.__elements.pop()
        self.__tot_len -= 1
        return i

    def draw(self, *args, **kwargs) -> None:
        if "elements_args" in kwargs:
            elements_args = kwargs["elements_args"]
            del kwargs["elements_args"]
        else:
            elements_args = []

        new_image = pygame.Surface(self.__size)
        new_image.fill(self.bg_color)

        for i, e in enumerate(self.__elements):
            try:
                e_args = elements_args[i]
            except IndexError:
                e_args = [None]
            if isinstance(e_args, list):
                e_args.insert(0, new_image)
                e.draw(*e_args)
            else:
                e_args["surface"] = new_image
                e.draw(**e_args)

        self.change_image(new_image)
        self.image.convert_alpha()

        super().draw(*args, **kwargs)


class AniSurfaceElement(SurfaceElement, AniElement):
    pass
