from abc import ABC, abstractmethod
from gui.point import Point


class Scene(ABC):
    _delegate = None

    def __init__(self):
        self._canvas = None
        self.is_quit = False
        self.is_changing_scene = False
        self.scene_id = ""
        
    @property
    def delegate(self):
        return self._delegate
        
    @delegate.setter
    def delegate(self, obj):
        self._delegate = obj

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, value):
        self._canvas = value

    @abstractmethod
    def ready(self):
        pass

    @abstractmethod
    def handle_events(self, event):
        pass

    @abstractmethod
    def update(self, time):
        pass

    @abstractmethod
    def render(self):
        pass

    @abstractmethod
    def unload(self):
        pass

    def request_quit(self):
        self.is_quit = True

    def request_scene_change(self, scene_id):
        self.is_changing_scene = True
        self.scene_id = scene_id
