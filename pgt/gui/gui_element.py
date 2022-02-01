#!/usr/bin/env python3

from pgt.constants import ABSOLUTE
from pgt.element import Element, AniElement


class GUIElement(Element):
    def __init__(self,
                 layout=None,
                 position_mode=ABSOLUTE,
                 *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = layout
        self.position_mode = position_mode

    def set_layout(self, new_layout):
        self.layout = new_layout
        if not self.is_anchored:
            self.anchor(new_layout, self._a_point)


class GUIAniElement(GUIElement, AniElement):
    pass
