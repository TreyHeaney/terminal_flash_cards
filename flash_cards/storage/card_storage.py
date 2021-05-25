'''Functions pertaining to persistent card storage.'''

import os
import requests
import json

from flash_cards.cards import Group, Card
from flash_cards.storage.directories import token_path
from flash_cards.storage.server import server


def load_save(file, is_json=False):
    '''Load a json of card and group states.'''
    
    if not is_json:
        file = open(file)
        raw = json.load(file)
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


def save(groups, directory):
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

    with open(directory, 'w') as file:
        json.dump(dictionary, file)

    return dictionary


def pull_save():
    '''Pulls a save from the server.'''
    with open(token_path) as file:
        token_json = json.load(file)
        headers = {"authorization": token_json['authorization']}
        response = requests.get(server + '/save', headers=headers)
        groups = load_save(response.json(), is_json=True)

    return groups


def push_save(save):
    '''Pushes a save to the server.'''
    with open(token_path) as file:
        token_json = json.load(file)
        headers = {"authorization": token_json['authorization']}
        response = requests.post(server + '/save', json=save, headers=headers)

    return response
