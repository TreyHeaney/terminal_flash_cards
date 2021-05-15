from flash_cards.displays.page_template import Page
from flash_cards.displays.groups import PreviewGroupPage, EditGroupPage


class WelcomePage(Page):
    '''Initial page displayed.'''
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Home'

    def display(self):
        super().predisplay()

        print('''Welcome to flash cards!

a: Manage groups
b: View Groups''')
        
        super().display()

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a':
            self.context.add_page(EditGroupPage(self.context))
        elif key == 'b':
            self.context.add_page(PreviewGroupPage(self.context))
            