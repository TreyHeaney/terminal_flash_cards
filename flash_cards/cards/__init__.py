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
