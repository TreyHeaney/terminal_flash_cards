from os import stat_result
import requests
import json
from getpass import getpass
from flash_cards.displays.page_template import Page
from flash_cards.src.networking import account_auth

url = 'http://localhost:4444'


class SignUpPage(Page):
    '''Page for user sign ups.'''
    def __init__(self, context):
        super().__init__(context)
        self.name = 'Sign Up'
    
    def display(self):
        super().predisplay()

        user = input('Username: ')
        password = getpass('Password: ')

        _, message, _ = account_auth(user, password, new_account=True)

        self.context.message = message

        self.context.back()
        self.context.back()
        print('ENTER to complete sign up request.')


    def parse_input(self, key):
        super().parse_input(key)


class SignInPage(Page):
    '''Page for user sign ins.'''
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
            file = open('./static/token.json', 'w')
            json.dump(response.json(), file)

        self.context.back()
        self.context.back()
        print('ENTER to complete sign in request.')

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
