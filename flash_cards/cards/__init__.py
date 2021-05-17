class Card:
    '''A single card'''
    def __init__(self, question, answer, dummy_answers=[]):
        self.question = question
        self.answer = answer
        self.dummy_answers = dummy_answers


class Group:
    '''A group of cards.'''
    def __init__(self, name, description, cards=[]):
        self.name = name
        self.description = description
        self.cards = cards


# Dummy data for now.
groups = [
    Group('Arabic', '', [
            Card('How do you say hello?', 'Marhaban', ['Yo', 'Whats up', 'Hey bro']),
            Card('How do you say hello?', 'Marhaban', ['Yo', 'Whats up', 'Hey bro']),
            Card('How do you say hello?', 'Marhaban', ['Yo', 'Whats up', 'Hey bro']),
        ]),
    Group('C++', '', [
            Card('How do you say hello?', 'Marhaban', ['Yo', 'Whats up', 'Hey bro']),
            Card('How do you say hello?', 'Marhaban', ['Yo', 'Whats up', 'Hey bro']),
            Card('How do you say hello?', 'Marhaban', ['Yo', 'Whats up', 'Hey bro']),
        ]), 
]
