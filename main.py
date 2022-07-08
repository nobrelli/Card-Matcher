from engine import Engine
from scenes import *
from config_loader import load_config


def main():
    conf = load_config()
    if conf is None:
        print('Could not load config file.')
        return

    # Initialize the engine and create the window
    props = conf['window_props']
    engine = Engine.get_instance(props['title'],
                                 props['width'],
                                 props['height'])

    # Add scenes
    engine.scene_manager.add_scene('menu', MenuScene())
    engine.scene_manager.add_scene('game', GameScene())
    engine.scene_manager.add_scene('pause', PauseScene())
    engine.scene_manager.add_scene('winner', WinnerScene())
    engine.scene_manager.add_scene('lost', LostScene())

    # Set the default scene
    engine.scene_manager.set_scene('menu')

    # Start the engine
    engine.start()


if __name__ == '__main__':
    main()
