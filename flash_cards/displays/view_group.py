from flash_cards.groups import groups
from flash_cards.displays.page_template import Page
from flash_cards.displays.new_group import NewGroupPage


class ViewGroupPage(Page):
    def __init__(self, context):
        super().__init__(context)

    def display(self):
        print('Select a group of cards to view.\n')
        for index, group in enumerate(groups):
            print(f'{chr(index + 97)}: {group.name}')
        super().display()  

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a': 
            self.context.page_stack.append(NewGroupPage(self.context))
