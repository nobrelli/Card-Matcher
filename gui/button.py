import pygame as pg
from .texted import Texted
from .interactive import Interactive


class Button(Interactive, Texted):
    # States
    DEFAULT = 0
    HOVER = 1
    CLICK = 2

    _back_color_norm = pg.Color(0)
    _back_color_hover = pg.Color(0)
    _back_color_click = pg.Color(0)

    def __init__(self, name):
        self.name = name

    def set_state_color(self, state, color):
        match state:
            case self.DEFAULT:
                self._back_color_norm = color
                self._back_color = color
            case self.HOVER:
                self._back_color_hover = color
            case self.CLICK:
                self._back_color_click = color

    def handle_events(self, event):
        super().handle_events(event)
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    self.background_color = self._back_color_click
            # On click
            case pg.MOUSEBUTTONUP:
                self.background_color = self._back_color_norm
                if event.button == pg.BUTTON_LEFT and self.rect.collidepoint(event.pos):
                    self.background_color = self._back_color_norm
            # On hover
            case pg.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    if event.buttons[0] == pg.BUTTON_LEFT:
                        self.background_color = self._back_color_click
                    else:
                        self.background_color = self._back_color_hover
                else:
                    self.background_color = self._back_color_norm

    def render(self, canvas):
        if self.font is not None:
            font_surf_center = pg.Vector2(self.font_surface.get_size()) // 2
            rect = pg.draw.rect(
                canvas,
                self.background_color,
                self.rect,
                border_radius=self.border_radius
            )
            btn_text_pos = rect.center - font_surf_center
            canvas.blit(self.font_surface, btn_text_pos)
