'''Pages for managing and viewing groups of cards.'''

from flash_cards.cards import Group
from flash_cards.src.page_template import Page
from flash_cards.displays.cards import ViewCardsPage, ManageCardsPage
from flash_cards.accounts import current_user


class NewGroupPage(Page):
    '''Page for creation of a new group.'''
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Group Creation'

    def display(self):
        print('Creating a new group.\n')
        new_group = Group(
            input('Name of group: '),
            input('Short description: ')
        ) 
        current_user.card_groups.append(new_group)
        self.context.back()
        self.context.message = 'Group successfully created!'
        print('\nPress ENTER to complete group creation.')

    def parse_input(self, key):
        super().parse_input(key)


class EditGroupPage(Page):
    '''Page for editing an existing group.'''
    def __init__(self, context, group=None):
        super().__init__(context)
        self.groups = current_user.card_groups
        self.group = group
        self.name = 'Editing Groups'

    def display(self):
        super().predisplay()
        if self.group is None: 
            print('Select a group to edit.\n')
            print('0: Create a new group')
            for index, group in enumerate(self.groups):
                print(f'{index + 1}: {group.name}')
            super().display()
        else: 
            edited_group = self.groups[self.group]
            print(f'Editing card group "{edited_group.name}"\n')
            edited_group.name = input('New group name: ')
            edited_group.description = input('New group description: ')
            delete_group = input('Delete group? (type \'y\')\n') == 'y'
            if delete_group: delete_group = input('Are you sure? This will remove all cards within the group and their scores. (type \'y\')\n') == 'y'

            if delete_group: del self.groups[self.group]
            
            print('\nPress ENTER to finish editing group.')
            self.context.message = 'Group successfully ' + 'deleted!' if delete_group else 'edited!' 

            self.context.back()


    def parse_input(self, key):
        super().parse_input(key)
        if key == '0': 
            new_page = NewGroupPage(self.context)
            self.context.add_page(new_page)
        possible_groups = [str(x) for x in range(1, len(current_user.card_groups) + 1)]
        if key in possible_groups:
            index = int(key) - 1
            new_page = EditGroupPage(self.context, index)
            self.context.add_page(new_page)


class PreviewGroupPage(Page):
    '''Page for previewing a group before you start a session with cards.'''
    def __init__(self, context, group=None, verbose=False):
        super().__init__(context)
        self.groups = current_user.card_groups
        self.selected_group = group
        self.verbose = verbose
        self.name = 'Group Selection' if group is None else self.groups[group].name 
        self.name = 'Verbose Card View' if verbose else self.name

    def display(self):
        super().predisplay()

        if self.selected_group is None:
            print('Select a group of cards to view.\n')
            for index, group in enumerate(self.groups):
                print(f'{index}: {group.name}')
            print('\nm: Manage Groups')
        else:
            selected_group = self.groups[self.selected_group]
            print('CARDS IN GROUP:')
            for card in selected_group.cards:
                padding = ((80 - len(card.question)) * '~') if self.verbose else ''
                print(card.question + padding)

                if self.verbose:
                    print(f'ANSWER:       {card.answer}')
                    print(f'SCORE:        {card.score}')
                    print(f'WRONG STREAK: {card.wrong_streak}')
                    print(f'LAST CORRECT: {card.last_correct}')

            print('\ns: Start Session, m: Manage Cards, v: Verbose View')
        
        super().display(new_line=False)

    def parse_input(self, key):
        super().parse_input(key)
        if self.selected_group is None:
            group_count = len(self.groups)
            selectable_groups = [str(x) for x in range(group_count)]
            if key in selectable_groups:
                new_page = PreviewGroupPage(self.context, int(key))
                self.context.add_page(new_page)
            if key == 'm':
                new_page = EditGroupPage(self.context)
                self.context.add_page(new_page)
        else:
            if key == 's':
                cards = self.groups[self.selected_group].cards

                new_page = ViewCardsPage(self.context, cards)
                self.context.add_page(new_page)
            elif key == 'm':
                new_page = ManageCardsPage(self.context, self.selected_group)
                self.context.add_page(new_page)
            elif key == 'v':
                new_page = PreviewGroupPage(self.context,
                                        self.selected_group,
                                        verbose=True)
                self.context.add_page(new_page)
