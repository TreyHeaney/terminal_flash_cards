'''Pages for managing and viewing groups of cards.'''

from flash_cards.cards import Group
from flash_cards.cards.storage import groups
from flash_cards.displays.page_template import Page
from flash_cards.displays.cards import ViewCardsPage, ManageCardsPage


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
                print(f'{index}: {group.name}')
            super().display()  
        else:
            selected_group = groups[self.selected_group]
            print('CARDS IN GROUP:')
            for card in selected_group.cards:
                print(card.question)
            print('\ns: Start new session, m: Manage Cards, v: View verbose card details')
            super().display(new_line=False)

    def parse_input(self, key):
        super().parse_input(key)
        if self.selected_group is None:
            print(key)
            print([x for x in range(len(groups) + 1)])
            if key in [str(x) for x in range(len(groups))]:
                self.context.add_page(PreviewGroupPage(self.context, 0))
        else:
            if key == 's':
                cards = groups[self.selected_group].cards
                self.context.add_page(ViewCardsPage(self.context, cards))
            if key == 'm':
                self.context.add_page(ManageCardsPage(self.context, 
                                                      self.selected_group))
                # self.context.add_page(NewCardPage(self.context, 
                #                                   self.selected_group))

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
        self.name = 'Editing Groups'

    def display(self):
        super().predisplay()
        if self.group is None: 
            print('Select a group to edit.\n')
            print('a: Create a new group')
            for index, group in enumerate(groups):
                print(f'{chr(index + 98)}: {group.name}')
            super().display()
        else: 
            edited_group = groups[self.group]
            print(f'Editing card group "{edited_group.name}"\n')
            edited_group.name = input('New group name: ')
            edited_group.description = input('New group description: ')
            delete_group = input('Delete group? (type \'yes\')\n') == 'yes'
            
            if delete_group: del groups[self.group]
            
            self.context.back()

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a': 
            self.context.add_page(NewGroupPage(self.context))
        if key in [chr(x) for x in range(98, 98 + len(groups) + 1)]:
            index = ord(key) - 98
            self.context.add_page(EditGroupPage(self.context, index))
