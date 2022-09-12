from time import time
from random import choices, random


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


def draw_card(cards, recently_drawn, draw_strong=False):
    '''
    Draw a weighted random card from a group of cards.
    '''
    score_sum = sum([card.score for card in cards])
    if score_sum > 0: 0
        if not draw_strong:
            weights = [1 - card.score / score_sum for card in cards]
        else:
            weights = [card.score / score_sum for card in cards]
    else: 
        weights = [1 for _ in cards]
    
    random_card = choices(cards, weights)[0]
    while random_card in recently_drawn:
        random_card = choices(cards, weights)[0]
    
    return random_card