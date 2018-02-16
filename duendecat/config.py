import json
import os

CONFIG_FILE = os.path.join('duendecat', 'config.json')


def read():
    with open(CONFIG_FILE) as f:
        return json.load(f)


def write(config):
    with open(CONFIG_FILE) as f:
        f.write(json.dumps(config, indent=2))
