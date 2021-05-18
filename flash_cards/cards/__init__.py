from time import time


class Card:
    '''A single card'''
    def __init__(self, question, answer, dummy_answers=[], last_correct=time(), 
                 score=0.0, wrong_streak=0):
        self.question = question
        self.answer = answer
        self.dummy_answers = dummy_answers
        self.last_correct = last_correct
        self.score = score
        self.wrong_streak = wrong_streak


class Group:
    '''A group of cards.'''
    def __init__(self, name, description, cards=[]):
        self.name = name
        self.description = description
        self.cards = cards
