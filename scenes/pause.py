import pygame as pg

from scene import Scene
from gui import *


class PauseScene(Scene):
    def __init__(self):
        super().__init__()
        self.background = pg.image.load_basic('./assets/images/mainbg.bmp')
        self._gui: GUI = None

    def ready(self):
        screen_size = self.manager.canvas.get_size()

        self._gui = GUI(self.canvas)
        cont = Container(0, 0, screen_size[0], screen_size[1])

        lbl_title = Label('title')
        btn_resume = Button('btn_resume')
        btn_menu = Button('btn_menu')

        # Main title
        lbl_title.set_margins(bottom=20)
        lbl_title.set_font('Boby.otf', 50)
        lbl_title.antialiased = True
        lbl_title.set_text('GAME PAUSED', pg.Color(76, 58, 81))

        btn_resume.set_state_color(Button.DEFAULT, pg.Color(178, 80, 104))
        btn_resume.set_state_color(Button.HOVER, pg.Color(119, 67, 96))
        btn_resume.set_state_color(Button.CLICK, pg.Color(231, 171, 121))
        btn_resume.set_font('Florsn.ttf', 20)
        btn_resume.set_text('Resume', pg.Color(255, 255, 255))
        btn_resume.antialiased = True
        btn_resume.set_size(120, 50)
        btn_resume.border_radius = 10
        btn_resume.on_click = lambda: self.resume()

        btn_menu.set_state_color(Button.DEFAULT, pg.Color(178, 80, 104))
        btn_menu.set_state_color(Button.HOVER, pg.Color(119, 67, 96))
        btn_menu.set_state_color(Button.CLICK, pg.Color(231, 171, 121))
        btn_menu.set_font('Florsn.ttf', 20)
        btn_menu.set_text('Menu', pg.Color(255, 255, 255))
        btn_menu.antialiased = True
        btn_menu.set_size(120, 50)
        btn_menu.border_radius = 10
        btn_menu.on_click = lambda: self.request_scene_change('menu')

        cont.add_control(lbl_title)
        cont.add_control(btn_resume)
        cont.add_control(btn_menu)
        self._gui.add_control(cont)
        
    def resume(self):
        self.manager.get_scene('game').resume()
        self.request_scene_change('game')

    def handle_events(self, event):
        self._gui.handle_events(event)

    def update(self, time):
        pass

    def render(self):
        self.canvas.blit(self.background, (0, 0))
        self._gui.render()

    def unload(self):
        self._gui.unload()
