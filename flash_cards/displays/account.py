from getpass import getpass
from flash_cards.accounts import current_user
from flash_cards.src.page_template import Page
from flash_cards.src.networking import account_auth
from flash_cards.storage.token_storage import save_token

url = 'http://localhost:4444'


class SignUpPage(Page):
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Sign Up'
    
    def display(self):
        super().predisplay()

        user = input('Username: ')
        password = getpass('Password: ')

        _, server_message, _ = account_auth(user, password, new_account=True)

        self.context.message = server_message

        self.context.back()
        self.context.back()
        print('ENTER to complete sign up request.')


    def parse_input(self, key):
        super().parse_input(key)


class SignInPage(Page):
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Sign In'
    
    def display(self):
        super().predisplay()

        user = input('Username: ')
        password = getpass('Password: ')
        
        response, message, status = account_auth(user, password)

        self.context.message = message

        if status == 200:
            save_token(response)
            current_user.signed_in = True

        self.context.back().back()

        # The client still tries to accept input. Big design flaw...
        print('ENTER to complete sign in request.')


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
