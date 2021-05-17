from json import load

from flash_cards.cards import Group, Card


def load_save(directory):
    '''Load the saved json of card and group states.'''
    f = open(directory)
    raw = load(f)
    groups = []
    for group in raw:
        current_group = Group(group, '', load_cards(raw[group]))
        groups.append(current_group)
    
    return groups


def load_cards(cards):
    '''Load a set of cards from json format.'''
    parsed = []
    for card in cards:
        parsed.append(Card(question=card, 
                           answer=cards[card][0],
                           dummy_answers=cards[card][1:]))

    return parsed


def save_cards():
    '''Statically store cards in json format.'''
    pass


groups = load_save('./static/save.json')