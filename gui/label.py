import pygame as pg
from .texted import Texted


class Label(Texted):
    def __init__(self, name):
        self.name = name

    def render(self, canvas):
        if self.font is not None:
            canvas.blit(self.font_surface, self.rect)
