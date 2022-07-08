import pygame as pg


class CountDownTimer:
    def __init__(self, duration, callback, repeat=False):
        self.duration = duration  # ms
        self.on_timeout = callback
        self.start_ticks = 0
        self.remaining = 0
        self.pause_dur = 0
        self.pause_start = 0

        # Flags
        self.started = False
        self._pause = False
        self.repeat = repeat

    def start(self):
        self.started = True
        self.start_ticks = pg.time.get_ticks()

    def stop(self):
        self.started = False

    def pause(self):
        self._pause = True
        self.pause_start = pg.time.get_ticks()

    def resume(self):
        self._pause = False
        self.pause_dur = pg.time.get_ticks() - self.pause_start
        self.start_ticks += self.pause_dur

    def add(self, ms):
        self.start_ticks += ms

    def update(self):
        if self.started and not self._pause:
            end_ticks = pg.time.get_ticks()
            elapsed = end_ticks - self.start_ticks
            self.remaining = self.duration - elapsed
            if self.remaining <= 0:
                self.on_timeout()
                if not self.repeat:
                    self.start_ticks = 0
                    self.remaining = 0
                    self.started = False
                else:
                    self.start_ticks = pg.time.get_ticks()
