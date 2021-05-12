from flash_cards.displays.page_template import Page
from flash_cards.groups import groups, Group


class NewGroupPage(Page):
    def __init__(self, context):
        super().__init__(context)

    def display(self):
        print('Creating a new group.\n')
        new_group = Group(
            input('Name of group: '),
            input('Short description: ')
        ) 
        groups.append(new_group)
        self.context.back()

    def parse_input(self, key):
        super().parse_input(key)
