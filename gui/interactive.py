import pygame as pg
from .component import Component


class Interactive(Component):
    _onclick = None
    _onhover = None

    mouse_button_down = False
    mouse_button_up = False
    mouse_over = False
    mouse_out = False
    dragging = False

    @property
    def on_click(self):
        return self._onclick

    @on_click.setter
    def on_click(self, func):
        if callable(func):
            self._onclick = func
        else:
            raise TypeError('"func" must be callable')

    @property
    def on_hover(self):
        return self._onhover

    @on_hover.setter
    def on_hover(self, func):
        if callable(func):
            self._onhover = func
        else:
            raise TypeError('"func" must be callable')

    def handle_events(self, event):
        match event.type:
            case pg.MOUSEBUTTONDOWN:
                if event.button == pg.BUTTON_LEFT and self.rect.collidepoint(event.pos):
                    self.mouse_button_down = True
                    self.mouse_button_up = False
                    self.mouse_over = True

                    if self.on_click is not None:
                        self.on_click()
            case pg.MOUSEBUTTONUP:
                if event.button == pg.BUTTON_LEFT and self.rect.collidepoint(event.pos):
                    self.mouse_button_down = False
                    self.mouse_button_up = True
                    self.mouse_over = True
            case pg.MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.mouse_over = True
                    self.mouse_out = False

                    if event.buttons[0] == pg.BUTTON_LEFT:
                        dragging = True
                    else:
                        dragging = False

                    if self.on_hover is not None:
                        self.on_hover()
                else:
                    self.mouse_over = False
                    self.mouse_out = True
