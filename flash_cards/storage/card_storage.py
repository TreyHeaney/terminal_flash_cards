'''Functions pertaining to persistent card storage.'''

import os
import requests
from json import load, dump

from flash_cards.cards import Group, Card
from flash_cards.storage.directories import token_path

server = 'http://localhost:4444'  # Offload this to an .env or something.


def load_save(file, is_json=False):
    '''Load a json of card and group states.'''
    
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


def save(groups, directory):
    '''store cards in json format.'''
    dictionary = {}
    for group in groups:
        dictionary[group.name] = {}
        curr_group = dictionary[group.name]
        for card in group.cards:
            curr_group[card.question] = {}
            curr_question = curr_group[card.question]
            curr_question['meta'] = {}
            
            curr_question['answers'] = [card.answer] + card.dummy_answers
            curr_question['meta']['score'] = card.score
            curr_question['meta']['wrong_streak'] = card.wrong_streak
            curr_question['meta']['last_correct'] = card.last_correct

    with open(directory, 'w') as file:
        dump(dictionary, file)


def pull_save():
    '''Pulls a save from the server'''
    with open(token_path) as file:
        token_json = load(file)
        headers = {"authorization": token_json['authorization']}
        response = requests.get(server + '/save', headers=headers)
        groups = load_save(response.json(), is_json=True)

    return groups
