#!/usr/bin/env python3

from pygame import mouse, Surface, transform

from .button import Button
from .gui_element import GUIElement
from pgt.constants import ABSOLUTE, AUTOMATIC
from pgt.mathf import Pos, Size
from pgt.element import Element
from pgt.type_hints import _col_type, _pos
from pgt.utils import filled_surface


class GUILayout(GUIElement):
    def __init__(self,
                 elements: dict[str: Element],
                 bg_color: _col_type = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bg_color = bg_color
        if self.bg_color is not None:
            self.image = filled_surface(self.size, self.bg_color)
        self.current_button_hint = None

        self.elements = []

        for name, element in elements.items():
            setattr(self, name, element)
            self.elements.append(element)
            if not isinstance(element, GUIElement):
                element.anchor(self)
                continue

            element.set_layout(self)
        self._calculate_autopos_offsets()
        self.buttons = list(filter(lambda x: isinstance(x, Button | GUILayout),
                                   self.elements))

    def _calculate_autopos_offsets(self):
        max_h = 0
        curr_y = 0
        curr_x = 0

        for e in self.elements:
            if not isinstance(e, GUIElement) or e.position_mode != AUTOMATIC:
                continue

            offset = e.padding_ul + Pos(0, curr_y)
            if curr_x + e.w <= self.w or e.w > self.w and curr_x == 0:
                offset.x += curr_x
                curr_x += e.w
                if e.h > max_h:
                    max_h = e.h
            else:
                offset.y += max_h
                curr_y += max_h
                max_h = e.h
                curr_x = e.w
            e.offset = offset

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
        if self.bg_color is None: return
        self.image = filled_surface(self.size, self.bg_color)
        self._calculate_autopos_offsets()

    def rotate(self, *args, **kwargs):
        raise NotImplemented("Rotating GUILayout is not supported")

    def scale(self, *args, **kwargs):
        raise NotImplemented("Scaling GUILayout is not supported")

    def change_image(self, surface):
        self.image = transform.scale(surface, self.true_size)

    def collide_point(self, point: _pos) -> bool:
        for i in self.elements:
            if i.collide_point(point):
                return True
        return False

    def auto_run(self):
        for i in self.buttons:
            if i.auto_run(): return True
        return False

    def show(self):
        for i in self.elements:
            i.show()
        super().show()

    def hide(self):
        for i in self.elements:
            i.hide()
        super().hide()

    def set_layout(self, new_layout):
        self.anchor(new_layout)
        self.layout = new_layout
        for i in self.elements:
            if isinstance(i, GUIElement):
                i.layout = new_layout

    def draw(self, *args, **kwargs):
        super().draw(*args, **kwargs)

        for i in self.elements:
            i.draw(*args, **kwargs)

        if self.hidden: return

        for i in reversed(self.buttons):
            if i.auto_run():
                return

        if self.current_button_hint:
            mouse_pos = Pos(mouse.get_pos())
            if mouse_pos.y - self.current_button_hint[1].size.h < 0:
                attr = "u"
            else:
                attr = "d"

            if self.current_button_hint[1].size.w + mouse_pos.x > self.size.w:
                attr += "r"
            else:
                attr += "l"

            setattr(self.current_button_hint[1], attr, mouse_pos)

            self.current_button_hint[1].draw(*args, **kwargs)
            self.current_button_hint[2].draw(*args, **kwargs)
