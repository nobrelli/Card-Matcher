import os.path

import pygame as pg
from .drawable import Drawable


class Texted(Drawable):
    _font: pg.font.Font = None
    _font_surf: pg.Surface = None

    _text = ""
    _font_name = "arial"
    _font_size = 12
    _font_color = pg.Color(0)
    _antialiased = False

    @property
    def font(self):
        return self._font

    @property
    def font_surface(self):
        return self._font_surf

    @property
    def text(self):
        return self._text

    @property
    def font_color(self):
        return self._font_color

    def set_text(self, value, color):
        self._text = value
        self._font_color = color

        if self.font is not None:
            self._font_surf = self.font.render(
                self.text,
                self.antialiased,
                self.font_color
            )
            self.rect = self._font_surf.get_rect()
        else:
            raise Exception('Specify a _font first')

    def set_font(self, font_name, font_size):
        self._font_name = font_name
        self._font_size = font_size

        # Check if the _font is a system _font or not
        if font_name in pg.font.get_fonts():
            self._font = pg.font.SysFont(font_name, font_size)
        else:
            font_name = os.path.abspath('./assets/fonts/' + font_name)
            self._font = pg.font.Font(font_name, font_size)

    @property
    def antialiased(self):
        return self._antialiased

    @antialiased.setter
    def antialiased(self, value: bool):
        self._antialiased = value
        self.set_text(self.text, self.font_color)

