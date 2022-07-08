import pygame as pg
from colors import Colours
from scene_manager import SceneManager


class Engine:
    _scene_manager: SceneManager = None

    instance = None
    running = False
    canvas = None

    FPS = 60
    FLAGS = pg.HWSURFACE | pg.DOUBLEBUF | pg.SCALED

    def __init__(self, title, width, height, clear_color=Colours.WHITE):
        if Engine.instance is not None:
            raise Exception(f'Only one {__name__} instance can be created.')
        else:
            Engine.instance = self

            Engine.title = title
            Engine.width = width
            Engine.height = height
            Engine.clear_color = clear_color

            pg.init()
            Engine.create_window()
            Engine._scene_manager = SceneManager.get_instance()
            SceneManager.canvas = Engine.canvas

    @property
    def scene_manager(self):
        return self._scene_manager

    @staticmethod
    def get_instance(title, width, height, clear_color=Colours.WHITE):
        """Engine singleton"""
        if Engine.instance is None:
            Engine(title, width, height, clear_color)

        return Engine.instance

    def start(self):
        self.running = True
        self.loop()

    def stop(self):
        self.running = False
        self.scene_manager.unload()
        pg.quit()

    @staticmethod
    def create_window():
        WINDOW_DIM = (Engine.width, Engine.height)
        Engine.canvas = pg.display.set_mode(WINDOW_DIM, Engine.FLAGS, vsync=1)
        pg.display.set_caption(Engine.title)

    def loop(self):
        clock = pg.time.Clock()

        while self.running:
            # Limit frame rate
            dt = clock.tick(self.FPS) / 1000

            if self.scene_manager.demands_quit():
                self.stop()
                break

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.stop()
                    return

                self.handle_events(event)

            self.update(dt)
            self.render()

    def handle_events(self, event):
        self.scene_manager.handle_events(event)

    def update(self, dt):
        self.scene_manager.update(dt)

    def render(self):
        self.canvas.fill(self.clear_color)
        self.scene_manager.render()
        pg.display.flip()
