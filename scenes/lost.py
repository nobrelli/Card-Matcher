import pygame as pg

from scene import Scene
from gui import *


class LostScene(Scene):
    def __init__(self):
        super().__init__()
        self.background = pg.image.load_basic('./assets/images/lostbg.bmp')
        self.gui: GUI = None

    def ready(self):
        canvas_size = self.manager.canvas.get_size()
        self.gui = GUI(self.canvas)
        container = Container(0, 0, canvas_size[0], canvas_size[1])

        lbl_title = Label('title')
        btn_try = Button('btn_next')
        btn_menu = Button('btn_menu')

        lbl_title.set_margins(bottom=20)
        lbl_title.set_font('Boby.otf', 50)
        lbl_title.antialiased = True
        lbl_title.set_text('YOU LOST', pg.Color(76, 58, 81))

        btn_try.set_state_color(Button.DEFAULT, pg.Color(178, 80, 104))
        btn_try.set_state_color(Button.HOVER, pg.Color(119, 67, 96))
        btn_try.set_state_color(Button.CLICK, pg.Color(231, 171, 121))
        btn_try.set_font('Florsn.ttf', 20)
        btn_try.set_text('Try again', pg.Color(255, 255, 255))
        btn_try.antialiased = True
        btn_try.set_size(120, 50)
        btn_try.border_radius = 10
        btn_try.on_click = lambda: self.repeat_level()

        btn_menu.set_state_color(Button.DEFAULT, pg.Color(178, 80, 104))
        btn_menu.set_state_color(Button.HOVER, pg.Color(119, 67, 96))
        btn_menu.set_state_color(Button.CLICK, pg.Color(231, 171, 121))
        btn_menu.set_font('Florsn.ttf', 20)
        btn_menu.set_text('Menu', pg.Color(255, 255, 255))
        btn_menu.antialiased = True
        btn_menu.set_size(120, 50)
        btn_menu.border_radius = 10
        btn_menu.on_click = lambda: self.request_scene_change('menu')

        container.add_control(lbl_title)
        container.add_control(btn_try)
        container.add_control(btn_menu)
        self.gui.add_control(container)

    def repeat_level(self):
        self.manager.get_scene('game').prepare_level()
        self.request_scene_change('game')

    def handle_events(self, event):
        self.gui.handle_events(event)

    def update(self, time):
        pass

    def render(self):
        self.canvas.blit(self.background, (0, 0))
        self.gui.render()

    def unload(self):
        pass
