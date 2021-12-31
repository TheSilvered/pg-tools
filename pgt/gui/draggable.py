from typing import Optional
import pygame.mouse
from pgt.element import MouseInteractionAniElement


class Draggable(MouseInteractionAniElement):
    def __init__(self,
                 button: int = 0,
                 locked: bool = False,
                 boundary_top: Optional[int] = None,
                 boundary_left: Optional[int] = None,
                 boundary_right: Optional[int] = None,
                 boundary_bottom: Optional[int] = None,
                 *args, **kwargs):

        super().__init__(*args, **kwargs)
        self.button = button
        self.dragging = False
        self.drag_point = (0, 0)
        self.locked = locked
        self.b_top = boundary_top
        self.b_right = boundary_right
        self.b_left = boundary_left
        self.b_bottom = boundary_bottom

    @property
    def button_clicked(self):
        return self.clicked[self.button]

    def fix_pos(self):
        if self.b_top is not None and self.u < self.b_top:
            self.u = self.b_top
        if self.b_bottom is not None and self.d > self.b_bottom:
            self.d = self.b_bottom
        if self.b_left is not None and self.l < self.b_left:
            self.l = self.b_left
        if self.b_right is not None and self.r > self.b_right:
            self.r = self.b_right

    def draw(self, *args, **kwargs):
        if not self.dragging and self.button_clicked and not self.locked:
            self.dragging = True
            self.drag_point = self.get_mouse_pos() - self.pos
        elif not pygame.mouse.get_pressed(3)[self.button]:
            self.dragging = False

        if self.dragging:
            self.pos = self.get_mouse_pos() - self.drag_point

        self.fix_pos()

        super().draw(*args, **kwargs)
