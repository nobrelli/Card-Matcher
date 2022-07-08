import pygame as pg

from scene import Scene
from colors import Colours


class SceneManager:
    instance = None

    _canvas: pg.Surface = None

    scenes = {}
    current_scene: Scene = None
    next_scene: Scene = None

    def __init__(self):
        if SceneManager.instance is not None:
            raise Exception(f'Only one {__name__} instance can be created.')
        else:
            SceneManager.instance = self

    @property
    def canvas(self):
        return self._canvas

    @canvas.setter
    def canvas(self, value):
        self._canvas = value

    @staticmethod
    def get_instance():
        if SceneManager.instance is None:
            SceneManager()

        return SceneManager.instance

    def handle_events(self, event):
        if self.current_scene:
            self.current_scene.handle_events(event)

    def demands_quit(self):
        return self.current_scene.is_quit

    def update(self, time):
        if self.current_scene.is_changing_scene:
            SceneManager.set_scene(self.current_scene.scene_id)
            self.current_scene.is_changing_scene = False
            self.current_scene.scene_id = ""
        else:
            self.current_scene.update(time)

    def render(self):
        if self.current_scene:
            self.current_scene.canvas.fill(Colours.WHITE)
            self.current_scene.render()
            # Draw the entire scene
            self.canvas.blit(self.current_scene.canvas, (0, 0))

    def unload(self):
        for scene in self.scenes.values():
            scene.unload()
        self.scenes.clear()

    @staticmethod
    def get_scene(scene_id):
        # Search if the scene exists in the list
        if SceneManager.scene_exists(scene_id):
            return SceneManager.scenes[scene_id]
        else:
            raise Exception(f'Scene "{scene_id}" does not exist.')

    @staticmethod
    def set_scene(scene_id):
        # Search if the scene exists in the list
        if SceneManager.scene_exists(scene_id):
            SceneManager.current_scene = SceneManager.scenes[scene_id]
        else:
            raise Exception(f'Scene "{scene_id}" does not exist.')

    @staticmethod
    def scene_exists(scene_id):
        for sid, scene in SceneManager.scenes.items():
            if scene_id == sid:
                return True

        return False

    @staticmethod
    def add_scene(scene_id, scene):
        # Assign the scene's manager as delegate
        scene.manager = SceneManager.instance

        # Create a canvas for that scene
        scene.canvas = pg.Surface(SceneManager.canvas.get_size())

        # Ready the scene
        scene.ready()

        # Add to the scenes list
        SceneManager.scenes[scene_id] = scene
