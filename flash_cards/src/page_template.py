from flash_cards.storage.card_storage import push_save, save
from flash_cards.storage.settings_storage import save_settings
from flash_cards.storage.directories import cached_save_path
from flash_cards.accounts import current_user


class Page:
    def __init__(self, context):
        self.context = context
        self.name = 'page'

    def display(self, new_line=True):
        print(('\n' if new_line else '') + 'q: Quit, `: Back Page')

    def predisplay(self):
        print(' -> '.join([page.name for page in self.context.page_stack]))
        message = self.context.message
        if message:
            print(message)
        print('')

    def parse_input(self, key):
        if key == 'q':
            save_dict = save(current_user.card_groups, 
                             current_user.settings['save_location'])

            using_remote_save = current_user.settings['save_location'] == cached_save_path
            if using_remote_save: push_save(save_dict)

            save_settings(current_user.settings)

            quit()
        elif key == '`':
            page_count = len(self.context.page_stack)
            
            if page_count > 1: self.context.back()
