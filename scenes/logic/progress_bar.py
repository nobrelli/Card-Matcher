import pygame as pg
from gui import Point, Size


class ProgressBar:
    def __init__(self, position: Point, size: Size, color, alt_state=None):
        self._position = position
        self._size = size
        self._current_width = 0
        self._new_width = 0
        # self._easer = Easer(Easing.EASE_IN_OUT_CUBIC)
        self._progress = 0
        self.color = color
        self.alt_state = alt_state
        self.toggled = False

    @property
    def progress(self):
        return self._progress

    @progress.setter
    def progress(self, value):
        self._progress = value
        # self._easer.begin()

    def toggle_state(self):
        self.toggled = True if not self.toggled else False

    def update(self, time):
        # self._easer.update(time)

        # easing_state = self._easer.get_state()
        # prog = self._size.width * self.progress - self._current_width
        # self._new_width = (self._current_width + prog) * easing_state
        # Growing or shrinking?
        segment = self._size.width * self._progress - self._current_width
        self._new_width = (self._current_width + segment)

    def render(self, canvas):
        col = self.color if not self.toggled else self.alt_state
        rect = pg.draw.rect(canvas, col, (
            self._position.X,
            self._position.Y,
            self._new_width,
            self._size.height
        ))
        self._current_width = rect.width