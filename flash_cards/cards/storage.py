'''Functions pertaining to persistent card storage.'''

import os
import requests
from json import load, dump

from flash_cards.cards import Group, Card

server = 'http://localhost:4444'


def load_save(file, is_json=False):
    '''Load the saved json of card and group states.'''
    if not is_json:
        file = open(file)
        raw = load(file)
    else:
        raw = file

    groups = []
    for group in raw:
        current_group = Group(group, '', load_cards(raw[group]))
        groups.append(current_group)
    
    if not is_json: file.close()

    return groups


def load_cards(cards):
    '''Load a set of cards from json format.'''
    parsed = []
    for card in cards:
        parsed.append(Card(question=card, 
                           answer=cards[card]['answers'][0],
                           dummy_answers=cards[card]['answers'][1:],
                           score=cards[card]['meta']['score'],
                           wrong_streak=cards[card]['meta']['wrong_streak'],
                           last_correct=cards[card]['meta']['last_correct']))

    return parsed


def save(groups):
    '''Statically store cards in json format.'''
    dictionary = {}
    for group in groups:
        dictionary[group.name] = {}
        for card in group.cards:
            dictionary[group.name][card.question] = {}
            dictionary[group.name][card.question]['meta'] = {}
            
            dictionary[group.name][card.question]['answers'] = [card.answer] + card.dummy_answers
            dictionary[group.name][card.question]['meta']['score'] = card.score
            dictionary[group.name][card.question]['meta']['wrong_streak'] = card.wrong_streak
            dictionary[group.name][card.question]['meta']['last_correct'] = card.last_correct

    file = open('./static/save.json', 'w')
    dump(dictionary, file)


def pull_save():
    '''Pulls a save from the server'''
    file = open('./static/token.json')
    
    parsed_json = load(file)
    headers = {"authorization": parsed_json['authorization']}
    response = requests.get(server + '/save', headers=headers)
    groups = load_save(response.json(), is_json=True)

    file.close()

local_save_exists = os.path.exists('./static/save.json')
user_logged_in = False  # os.path.exists('./static/token.json')
if user_logged_in:
    groups = pull_save()
else:
    if local_save_exists:
        groups = load_save('./static/save.json')
    else:
        groups = []