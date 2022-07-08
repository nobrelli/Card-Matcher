import pygame as pg

from scene import Scene
from gui import *


class MenuScene(Scene):
    def __init__(self):
        super().__init__()
        self.background = pg.image.load_basic('./assets/images/mainbg.bmp')
        self.gui: GUI = None

    def ready(self):
        screen_size = self.canvas.get_size()

        self.gui = GUI(self.canvas)
        cont = Container(0, 0, screen_size[0], screen_size[1])

        lbl_title = Label('title')
        btn_play = Button('btn_play')
        btn_quit = Button('btn_quit')

        # Main title
        lbl_title.set_margins(bottom=20)
        lbl_title.set_font('Boby.otf', 50)
        lbl_title.antialiased = True
        lbl_title.set_text('Match the Cards', pg.Color(76, 58, 81))

        # Play button
        btn_play.set_state_color(Button.DEFAULT, pg.Color(178, 80, 104))
        btn_play.set_state_color(Button.HOVER, pg.Color(119, 67, 96))
        btn_play.set_state_color(Button.CLICK, pg.Color(231, 171, 121))
        btn_play.set_font('Florsn.ttf', 20)
        btn_play.set_text('Play', pg.Color(255, 255, 255))
        btn_play.antialiased = True
        btn_play.set_size(120, 50)
        btn_play.border_radius = 10
        btn_play.on_click = lambda: self.start_game()

        # Quit button
        btn_quit.set_state_color(Button.DEFAULT, pg.Color(178, 80, 104))
        btn_quit.set_state_color(Button.HOVER, pg.Color(119, 67, 96))
        btn_quit.set_state_color(Button.CLICK, pg.Color(231, 171, 121))
        btn_quit.set_font('Florsn.ttf', 20)
        btn_quit.set_text('Quit', pg.Color(255, 255, 255))
        btn_quit.antialiased = True
        btn_quit.set_size(120, 50)
        btn_quit.border_radius = 10
        btn_quit.on_click = lambda: self.request_quit()

        cont.add_control(lbl_title)
        cont.add_control(btn_play)
        cont.add_control(btn_quit)
        self.gui.add_control(cont)

    def start_game(self):
        self.manager.get_scene('game').ready()
        self.request_scene_change('game')

    def handle_events(self, event):
        self.gui.handle_events(event)

    def update(self, time):
        pass

    def render(self):
        self.canvas.blit(self.background, (0, 0))
        self.gui.render()

    def unload(self):
        self.gui.unload()
