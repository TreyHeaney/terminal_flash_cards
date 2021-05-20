from flash_cards.displays.page_template import Page
from flash_cards.displays.groups import PreviewGroupPage, EditGroupPage
from flash_cards.displays.account import AccountPage


class WelcomePage(Page):
    '''Initial page displayed.'''
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Home'

    def display(self):
        super().predisplay()

        print(f'''   ______         __     _____            __    __
  / __/ /__ ____ / /    / ___/__ ________/ /__ / /
 / _// / _ `(_-</ _ \  / /__/ _ `/ __/ _  (_-</_/ 
/_/ /_/\_,_/___/_//_/  \___/\_,_/_/  \_,_/___(_)  
                                                  

a: Manage card groups
b: View card groups
c: {'Login or Signup'}''')
        
        super().display()

    def parse_input(self, key):
        super().parse_input(key)
        if key == 'a':
            new_page = EditGroupPage(self.context)
            self.context.add_page(new_page)
        elif key == 'b':
            new_page = PreviewGroupPage(self.context)
            self.context.add_page(new_page)
        elif key == 'c':
            new_page = AccountPage(self.context)
            self.context.add_page(new_page)