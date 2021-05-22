from json import load, dump
import os

from flash_cards.storage.directories import settings_path, local_save_path

default_settings = {
    'save_location': local_save_path
}


def load_settings():
    '''Load the saved json of user settings.'''
    if not os.path.exists(settings_path): return default_settings

    with open(settings_path) as file:
        settings = load(file)

    return settings


def save_settings(settings):
    '''Save user settings to json.'''
    with open(settings_path, 'w') as file:
        dump(settings, file)
