import json


def save_token(token):
    file = open('./static/token.json', 'w')
    json.dump(token.json(), file)
    file.close()
