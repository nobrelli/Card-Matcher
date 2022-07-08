import json


def load_config():
    with open('config.json') as conf:
        return json.load(conf)

    return None
