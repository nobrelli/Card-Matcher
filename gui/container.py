import pygame as pg
from .component import Component


class Alignment:
    LEFT = 0
    RIGHT = 1
    CENTER = 2


class Container(Component):
    SPACING = 5

    def __init__(self, left, top, width, height, alignment=Alignment.CENTER):
        self.rect = pg.Rect(left, top, width, height)
        self.alignment = alignment
        self.controls = []
        self._height = 0

    def add_control(self, control):
        self.controls.append(control)

        # Calculate the max contents height and re-align
        if len(self.controls) == 1:
            self._height = control.rect.height + control.margins.top + control.margins.bottom
        else:
            self._height += self.SPACING + control.rect.height + control.margins.top

        self.align_contents()

    def handle_events(self, event):
        for control in self.controls:
            control.handle_events(event)

    def render(self, canvas):
        for control in self.controls:
            control.render(canvas)

    def align_contents(self):
        if len(self.controls):
            for count, control in enumerate(self.controls):
                control.rect.center = self.rect.center

                # 2nd and nth element
                if count == 0:
                    control.rect.top = (self.rect.centery - self._height // 2) + control.margins.top
                else:
                    prev = self.controls[count - 1]
                    control.rect.top = prev.rect.bottom + prev.margins.bottom + control.margins.top + self.SPACING
