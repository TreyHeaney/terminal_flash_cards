'''Pages for managing and viewing groups of cards.'''

from flash_cards.cards import groups, Group
from flash_cards.displays.page_template import Page
from flash_cards.displays.cards import ViewCardsPage


class PreviewGroupPage(Page):
    '''Page for previewing a group before you start a session with cards.'''
    def __init__(self, context, group=None):
        super().__init__(context)
        self.selected_group = group
        self.name = 'Group Selection' if group is None else groups[group].name 

    def display(self):
        super().predisplay()
        if self.selected_group is None:
            print('Select a group of cards to view.\n')
            for index, group in enumerate(groups):
                print(f'{chr(index + 97)}: {group.name}')
            super().display()  
        else:
            selected_group = groups[self.selected_group]
            for card in selected_group.cards:
                print(f'{card.question}: {card.answer}')
            print('\ns: Start new session, n: New card, v: View verbose card details')
            super().display(new_line=False)

    def parse_input(self, key):
        super().parse_input(key)
        if self.selected_group is None:
            # This might cause some problems if the number of card reaches 'q'.
            if key in [chr(x) for x in range(97, 97 + len(groups) + 1)]:
                
                self.context.add_page(PreviewGroupPage(self.context, 0))
        else:
            if key == 's':
                self.context.add_page(ViewCardsPage(self.context))


class NewGroupPage(Page):
    '''Page for creation ofa new group.'''
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


class EditGroupPage(Page):
    '''Page for editing an existing group.'''
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
            
            if delete_group: del edited_group
            
            self.context.back()

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a': 
            self.context.add_page(NewGroupPage(self.context))
        if key in [chr(x) for x in range(98, 98 + len(groups) + 1)]:
            index = ord(key) - 98
            self.context.add_page(EditGroupPage(self.context, index))
