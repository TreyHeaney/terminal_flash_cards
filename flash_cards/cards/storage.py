from json import load, dump

from flash_cards.cards import Group, Card


def load_save(directory):
    '''Load the saved json of card and group states.'''
    with open(directory) as f:
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


def save(groups):
    '''Statically store cards in json format.'''
    dictionary = {}
    for group in groups:
        dictionary[group.name] = {}
        for card in group.cards:
            dictionary[group.name][card.question] = [card.answer] + card.dummy_answers

    file = open('./static/save.json', 'w')
    dump(dictionary, file)

    print(dictionary)


groups = load_save('./static/save.json')
