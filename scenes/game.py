import pygame as pg

from scene import Scene
from gui import Point
from .logic.card_grid import CardGrid


class GameScene(Scene):
    card_grid = None
    # row - col - time
    levels = [
        (3, 2, 5),
        (4, 3, 15),
        (4, 4, 25),
        (5, 4, 35),
        (6, 6, 45),
        (7, 6, 55),
        (8, 8, 65)
    ]
    level = 0
    SPACING = 5

    def __init__(self):
        super().__init__()
        self.background = pg.image.load_basic('./assets/images/mainbg.bmp')

    def ready(self):
        self.level = 1
        # Create the card grid
        self.prepare_level()

    def increase_level(self):
        self.level += 1
        self.prepare_level()

    def resume(self):
        self.card_grid.resume()

    def prepare_level(self):
        screen_size = pg.Vector2(self.manager.canvas.get_size()) // 2

        self.card_grid = CardGrid(
            self.canvas,
            Point(screen_size.x, screen_size.y),
            self.levels[self.level - 1][2],
            self.levels[self.level - 1][0],
            self.levels[self.level - 1][1],
            self.SPACING
        )
        self.card_grid.on_win = lambda: self.request_scene_change('winner')
        self.card_grid.on_lose = lambda: self.request_scene_change('lost')

    def handle_events(self, event):
        self.card_grid.handle_event(event)

        if event.type == pg.KEYUP:
            if event.key == pg.K_ESCAPE:
                self.card_grid.pause()
                self.request_scene_change('pause')

    def update(self, time):
        self.card_grid.update(time)

    def render(self):
        self.canvas.blit(self.background, (0, 0))
        self.card_grid.render()

    def unload(self):
        pass

    def is_quit(self):
        pass
