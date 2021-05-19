import getpass

from flash_cards.displays.page_template import Page


class SignUpPage(Page):
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Sign Up'
    
    def display(self):
        super().predisplay()
        super().display()

    def parse_input(self, key):
        super().parse_input(key)


class SignInPage(Page):
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Sign In'
    
    def display(self):
        super().predisplay()
        super().display()

    def parse_input(self, key):
        super().parse_input(key)


class AccountPage(Page):
    def __init__(self, context, login=None):
        super().__init__(context)
        self.name = 'Account'

    def display(self):
        super().predisplay()

        print('a: Sign in')
        print('b: Sign up')
        super().display()
    
    def parse_input(self, key):
        super().parse_input(key)

        if key == 'a':
            new_page = SignInPage(self.context)
            self.context.add_page(new_page)
        elif key == 'b':
            new_page = SignUpPage(self.context)
            self.context.add_page(new_page)
