from flash_cards.displays.page_template import Page
from flash_cards.displays.groups import PreviewGroupPage, EditGroupPage


class WelcomePage(Page):
    def __init__(self, context):
        super().__init__(context)

    def display(self):
        print('''Welcome to flash cards!

a: Create a new group
b: View Groups''')
        super().display()

    def parse_input(self, key):
        key = key.lower()
        if key == 'a':
            self.context.add_page(EditGroupPage(self.context))

        elif key == 'b':
            self.context.add_page(PreviewGroupPage(self.context))

        elif key == 'q':
            quit()
            