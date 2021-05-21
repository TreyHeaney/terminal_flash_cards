'''Page for managing saves.'''

from flash_cards.src.page_template import Page
from flash_cards.accounts import current_user
from flash_cards.storage.directories import local_save_path, cached_save_path


class ManageSavePage(Page):
    '''Page for managing saves'''
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Save Management'

    def display(self):
        super().predisplay()
        print(f'SAVE PATH: {current_user.settings["save_location"]}')
        print('''0: Use Local Save
1: Use Remote Save
2: Use Custom Save''')

        super().display()

    def parse_input(self, key):
        super().parse_input(key)
        if key == '0':
            current_user.settings['save_location'] = local_save_path
        elif key == '1':
            current_user.settings['save_location'] = cached_save_path
        elif key == '2':
            message = '\nPlease enter the absolute path to your save location.'
            user_input = input(message)
            if user_input:
                current_user.settings['save_location'] = user_input
