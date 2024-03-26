from flash_cards.accounts import current_user
from flash_cards.storage.card_storage import save
from flash_cards.storage.settings_storage import save_settings
from flash_cards.src.strings.basics import newline


class Page:
    def __init__(self, context):
        self.context = context
        self.name = 'page'

    def display(self, linebreak=True):
        nl = newline if linebreak else ''
        print(nl + 'q: Quit, `: Back Page')

    def predisplay(self):
        page_names = [page.name for page in self.context.page_stack]
        print(' -> '.join(page_names))
        message = self.context.message
        if message:
            print(message)
        print('')

    def parse_input(self, key):
        if key == 'q':
            save(current_user.card_groups, 
                 current_user.settings['save_location'])
            save_settings(current_user.settings)
            quit()
        elif key == '`':
            page_count = len(self.context.page_stack)
            
            if page_count > 1: self.context.back()
