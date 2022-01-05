from pgt.element import Element


class GUIElement(Element):
    def __init__(self, layout=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.layout = layout

    def set_layout(self, new_layout):
        self.layout = new_layout
        self.anchor(new_layout, self._a_point)
