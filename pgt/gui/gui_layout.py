from pygame import mouse, Surface

from .button import Button
from .gui_element import GUIElement
from pgt.mathf import Pos
from pgt.element import Element
from pgt.type_hints import _col_type, _pos


class GUILayout(GUIElement):
    def __init__(self,
                 elements: dict[str: Element],
                 elements_order: list[str],
                 bg_color: _col_type = None,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        if bg_color is not None:
            new_image = Surface(self.size)
            new_image.fill(bg_color)
            self.change_image(new_image)
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
                    f"elements_order got {set_eo - set_e} names not defined"
                )
        for i in elements_order:
            setattr(self, i, elements[i])
            self.elements.append(elements[i])
            if isinstance(elements[i], GUIElement):
                elements[i].set_layout(self)
            else:
                elements[i].anchor(self)

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
