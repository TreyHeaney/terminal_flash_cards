from flash_cards.accounts import current_user
from flash_cards.src.page_template import Page
from flash_cards.displays.groups import PreviewGroupPage, EditGroupPage
from flash_cards.displays.account import AccountPage
from flash_cards.displays.settings import SettingsPage
from flash_cards.displays.save_management import ManageSavePage


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
                                                  

a: View card groups
b: Manage Save
c: Settings
d: {'Sign in or sign up' if not current_user.signed_in else 'Sign out'}''')
        
        super().display()

    def parse_input(self, key):
        super().parse_input(key)

        # This is how a match-case should look
        # match x case y:
        #   expression()
        # case z:
        #   expression()
        # nocase: 
        #   expression()
        # the current syntax is horrifically ugly and unreadable but it won't
        # change because people actually implemented things with it. 
        if key == 'a':
            message = current_user.load_cards()  # hacky !!!
            if message: self.context.message = message

            new_page = PreviewGroupPage(self.context)
            self.context.add_page(new_page)
        elif key == 'b':
            new_page = ManageSavePage(self.context)
            self.context.add_page(new_page)
        elif key == 'c':
            new_page = SettingsPage(self.context)
            self.context.add_page(new_page)
        elif key == 'd':
            if current_user.signed_in:
                current_user.delete_token()
                self.context.message = 'Signed out successfully!'
            else:
                new_page = AccountPage(self.context)
                self.context.add_page(new_page)