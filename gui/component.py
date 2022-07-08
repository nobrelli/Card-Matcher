import pygame as pg
from functools import singledispatch


class Margin:
    def __init__(self, top=0, bottom=0, left=0, right=0):
        self.top = top
        self.bottom = bottom
        self.left = left
        self.right = right


class Component:
    _name = ""
    rect = pg.Rect(0, 0, 0, 0)
    _margins = Margin()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    def set_size(self, width, height):
        self.rect.width = width
        self.rect.height = height

    def set_position(self, x, y):
        self.rect.left = x
        self.rect.top = y

    @property
    def margins(self):
        return self._margins

    @singledispatch
    def set_margins(self, top=0, bottom=0, left=0, right=0):
        self._margins.top = top
        self._margins.bottom = bottom
        self._margins.left = left
        self._margins.right = right

    @set_margins.register
    def _(self, margins: Margin):
        self._margins = margins

    def handle_events(self, event):
        pass

    def render(self, canvas):
        pass
