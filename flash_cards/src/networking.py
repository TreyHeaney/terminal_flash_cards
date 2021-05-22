from os import stat_result
import requests
import json

url = 'http://localhost:4444'


def account_auth(user, password, new_account=False):
    route = '/sign_up' if new_account else '/sign_in'

    try:
        body = {'user': user, 'password': password}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url + route, 
                                 data=json.dumps(body), 
                                 headers=headers)
        
        status_code = response.status_code
        message = response.json()['message']
    except Exception as e:
        print(e)
        response = None
        status_code = 408
        message = 'Connection error. Local save will be used.'

    return response, message, status_code
