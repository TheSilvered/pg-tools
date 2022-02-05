#!/usr/bin/env python3
from typing import Optional

from pygame import display

from pgt.constants import ABSOLUTE
from pgt.element import Element, AniElement
from pgt.mathf import Pos, Size
from pgt.type_hints import _size


class GUIElement(Element):
    def __init__(self,
                 layout: Optional["Layout"] =None,
                 position_mode: int = ABSOLUTE,
                 rel_size: _size = Size(None),
                 padding_top: float = 0,
                 padding_bottom: float = 0,
                 padding_left: float = 0,
                 padding_right: float = 0,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.rel_size = Size(rel_size)
        self.layout = layout
        self.position_mode = position_mode
        self.padding_ul = round(Pos(padding_left,  padding_top))
        self.padding_dr = round(Pos(padding_right, padding_bottom))

    @property
    def size(self):
        size = Size(self.rect.size)
        size += self.padding_ul
        size += self.padding_dr
        return size

    @size.setter
    def size(self, value):
        value = round(Size(value))
        value -= self.padding_ul
        value -= self.padding_dr
        self.rect.size = value

    @property
    def true_size(self):
        return Size(self.rect.size)

    def set_layout(self, new_layout: "Layout"):
        self.layout = new_layout
        if not self.is_anchored:
            self.anchor(new_layout, self._a_point)

    def draw(self, *args, **kwargs):
        if self.layout:
            max_size = self.layout.size
        else:
            max_size = Size(display.get_window_size())

        if self.rel_size.w is not None:
            self.w = max_size.w * self.rel_size.w
        if self.rel_size.h is not None:
            self.h = max_size.h * self.rel_size.h
        super().draw(*args, **kwargs)


class GUIAniElement(GUIElement, AniElement):
    pass
