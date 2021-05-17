from flash_cards.displays.page_template import Page
from flash_cards.displays.groups import PreviewGroupPage, EditGroupPage


class WelcomePage(Page):
    '''Initial page displayed.'''
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Home'

    def display(self):
        super().predisplay()

        print('''   ______         __     _____            __    __
  / __/ ___ ____ / /    / ______ ________/ ___ / /
 / _// / _ `(_-</ _ \  / /__/ _ `/ __/ _  (_-</_/ 
/_/ /_/\_,_/___/_//_/  \___/\_,_/_/  \_,_/___(_)  
                                                  

a: Manage card groups
b: View card groups''')
        
        super().display()

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a':
            self.context.add_page(EditGroupPage(self.context))
        elif key == 'b':
            self.context.add_page(PreviewGroupPage(self.context))
            