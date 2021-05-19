import requests
import json
from getpass import getpass
from flash_cards.displays.page_template import Page

url = 'http://localhost:4444'


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

        user = input('Username: ')
        password = getpass('Password: ')

        body = {'user': user, 'password': password}
        headers = {'Content-Type': 'application/json'}
        res = requests.post(url + '/sign_in', 
                            data=json.dumps(body), 
                            headers=headers)
        
        res_json = res.json()

        print(res.status_code)
        print(dir(res))

        if res_json['message']:
            self.context.message = res_json['message']
        
        if res.status_code == 200:
            file = open('./static/token.json', 'w')
            json.dump(res_json, file)

        self.context.back()
        self.context.back()
        print('ENTER to complete login request.')

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
