#!/usr/bin/env python3

from pygame import mouse, Surface

from .button import Button
from .gui_element import GUIElement
from pgt.constants import ABSOLUTE, AUTOMATIC
from pgt.mathf import Pos
from pgt.element import Element
from pgt.type_hints import _col_type, _pos
from pgt.utils import filled_surface


class GUILayout(GUIElement):
    def __init__(self,
                 elements: dict[str: Element],
                 elements_order: list[str],
                 bg_color: _col_type = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        if bg_color is not None:
            self.change_image(filled_surface(self.size, bg_color))
        self.current_button_hint = None

        self.elements = []
        set_e = set(elements)
        set_eo = set(elements_order)

        # Any element that is not in elements_order but is in
        # elements is added without a specific order
        if set_e != set_eo:
            if set_e - set_eo:
                for i in set_e - set_eo:
                    elements_order.append(i)
            else:
                raise TypeError(
                    f"elements_order doesn't define {set_eo - set_e}"
                )

        max_h = 0
        curr_y = 0
        curr_x = 0

        for i in elements_order:
            element = elements[i]
            setattr(self, i, element)
            self.elements.append(element)
            if not isinstance(element, GUIElement):
                element.anchor(self)
                continue

            element.set_layout(self)
            if element.position_mode != AUTOMATIC: continue

            offset = Pos(0, curr_y)
            if curr_x + element.w <= self.w or element.w > self.w and curr_x == 0:
                offset.x += curr_x
                curr_x += element.w
                if element.h > max_h:
                    max_h = element.h
            else:
                offset.y += max_h
                curr_y += max_h
                max_h = element.h
                curr_x = element.w
            element.offset = offset

        self.buttons = list(filter(lambda x: isinstance(x, Button | GUILayout),
                                   self.elements))

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
        self.hidden = False

    def hide(self):
        for i in self.elements:
            i.hide()
        self.hidden = True

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
