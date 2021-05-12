class Group:
    '''A group of cards.'''
    def __init__(self, name, description, cards=[]):
        self.name = name
        self.description = description
        self.cards = cards


groups = [Group('Arabic', ''), Group('Quran', ''), Group('C++', '')]
