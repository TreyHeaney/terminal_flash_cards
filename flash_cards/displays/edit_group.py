from flash_cards.groups import groups
from flash_cards.displays.page_template import Page
from flash_cards.displays.new_group import NewGroupPage


class EditGroupPage(Page):
    def __init__(self, context, group=None):
        super().__init__(context)
        self.group = group

    def display(self):
        if self.group is None: 
            print('Select a group to edit.\n')
            print('a: New group')
            for index, group in enumerate(groups):
                print(f'{chr(index + 98)}: {group.name}')
            super().display()
        else: 
            edited_group = groups[self.group]
            print(f'Editing card group "{edited_group.name}"\n')
            edited_group.name = input('New group name: ')
            edited_group.description = input('New group description: ')
            delete_group = input('Delete group? (yes/no)\n') == 'yes'
            
            if delete_group: del groups[self.group]
            
            self.context.back()

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a': 
            self.context.page_stack.append(NewGroupPage(self.context))
        if key in [chr(x) for x in range(98, 98 + len(groups) + 1)]:
            index = ord(key) - 98
            self.context.page_stack.append(EditGroupPage(self.context, index))    