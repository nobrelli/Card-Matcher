import pygame as pg
from .component import Component


class Drawable(Component):
    _back_color = pg.Color(0)
    _outline_color = pg.Color(0)
    _outline_width = 0
    _border_radius = -1

    @property
    def background_color(self):
        return self._back_color

    @background_color.setter
    def background_color(self, value):
        self._back_color = value

    @property
    def outline_color(self):
        return self._outline_color

    @outline_color.setter
    def outline_color(self, value):
        self._outline_color = value

    @property
    def outline_width(self):
        return self._outline_width

    @outline_width.setter
    def outline_width(self, value):
        self._outline_width = value

    @property
    def border_radius(self):
        return self._border_radius

    @border_radius.setter
    def border_radius(self, value):
        self._border_radius = value
