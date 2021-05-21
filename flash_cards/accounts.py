from json import load
import os
from flash_cards.storage.settings_storage import load_settings
from flash_cards.storage.directories import cached_save_path
from flash_cards.storage.card_storage import load_save, save, pull_save



class User:
    def __init__(self):
        self.signed_in = os.path.exists('./static/token.json')
        self.settings = load_settings()

        self.load_cards()

    def delete_token(self):
        os.remove('./static/token.json')
        self.signed_in = False

    def load_cards(self):
        save_path = self.settings['save_location']
        # This logic is bloated.
        message = ''
        if save_path == cached_save_path:
            try:
                groups = pull_save()
            except:
                if os.path.exists(cached_save_path): 
                    message = 'Connection error. Using cached remote save.'
                    groups = load_save(cached_save_path)
                else: 
                    message = 'Connection error.'
                    groups = []
        else:
            if os.path.exists(save_path):
                groups = load_save(save_path)
            else: groups = []

        self.card_groups = groups
        return message


current_user = User()