import os


class UserAccount:
    def __init__(self):
        self.signed_in = os.path.exists('./static/token.json')

    def delete_token(self):
        os.remove('./static/token.json')
        self.signed_in = False


current_user = UserAccount()