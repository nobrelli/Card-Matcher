import pygame as pg


class Card:
    def __init__(self, font):
        self._color = pg.Color(0)
        self._rect = pg.Rect(0, 0, 0, 0)
        self._address = (0, 0)
        self._text = ""
        self._paired = False
        self._flipped = False
        self._font: pg.font.Font = font
        self._font_surf = None

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        self._color = color

    @property
    def rect(self):
        return self._rect

    @rect.setter
    def rect(self, rect):
        self._rect = rect

    @property
    def address(self):
        """Address/cell location of this card"""
        return self._address

    @address.setter
    def address(self, address: tuple):
        self._address = address

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text
        self._font_surf = self._font.render(self.text, False, (255, 255, 255))

    @property
    def paired(self):
        return self._paired

    @paired.setter
    def paired(self, value):
        self._paired = value

    def __repr__(self):
        return str(f'Card at {self.address}')

    def flip(self):
        self._flipped = False if self._flipped else True

    def is_flipped(self):
        return self._flipped

    def detect_click(self):
        return self._rect.collidepoint(pg.mouse.get_pos())

    def render(self, canvas: pg.Surface):
        temp_color = (255, 255, 255) if not self.is_flipped() else self.color

        pg.draw.rect(
            canvas,
            temp_color,
            self.rect
        )

        canvas.blit(self._font_surf, (
            self._rect.center[0] - self._font_surf.get_width() / 2,
            self._rect.center[1] - self._font_surf.get_height() / 2
        ))
        
