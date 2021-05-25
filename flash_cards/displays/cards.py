'''Pages for viewing or managing cards.'''

import os
import random
import time
from collections import deque
from random import choices, shuffle

from flash_cards.cards import Card, draw_card
from flash_cards.accounts import current_user
from flash_cards.os_switches import clear_terminal
from flash_cards.src.colors import colors
from flash_cards.src.page_template import Page
from flash_cards.src.score_calculations import calculate_points, calculate_loss


class ViewCardsPage(Page):
    '''View a single card and guess the answer.'''
    def __init__(self, context, cards=[]):
        super().__init__(context)
        self.name = 'Viewing Cards'
        self.cards = cards
        max_history = int(len(self.cards) * 0.4)
        self.recently_drawn = deque([], maxlen=max_history)
        self.last_correct = True

    def display(self):
        super().predisplay()
        random_card = draw_card(self.cards, 
                                self.recently_drawn,
                                draw_strong=not self.last_correct)

        self.recently_drawn.append(random_card)

        self.last_score = random_card.score
        print(f'Card Strength: {random_card.score}')
        print(random_card.question + '\n')

        # Shuffle the answers.
        shuffle(random_card.dummy_answers)
        answers = random_card.dummy_answers[:3] + [random_card.answer]
        shuffle(answers)
        for number, answer in enumerate(answers):
            letter = chr(97 + number)
            print(f'{letter}: {answer}')

        self.answers = answers
        self.card = random_card
        super().display()

    def parse_input(self, key):
        super().parse_input(key)

        if len(key) != 1: return

        alphabet_start_ord = 97
        key_index = ord(key) - alphabet_start_ord
        if key_index not in [x for x in range(len(self.answers))]: return

        card = self.card
        answer_is_correct = self.answers[key_index] == card.answer
        if answer_is_correct:
            time_since_correct = time.time() - card.last_correct
            card.score += calculate_points(time_since_correct,
                                           card.wrong_streak)
            card.score = min((100, card.score))

            card.wrong_streak = 0

            card.last_correct = time.time()
            
            self.last_correct = True
        else:
            card.wrong_streak += 1

            card.score -= calculate_loss(card.wrong_streak)
            card.score = max((0, card.score))

            self.last_correct = False

        self.display_answer(key_index)

    def display_answer(self, key_index):
        os.system(clear_terminal)
        super().predisplay()

        print(f'Card Strength: {self.last_score} -> {self.card.score}')
        print(self.card.question + '\n')

        for number, answer in enumerate(self.answers):
            pre_text = ''
            letter = chr(97 + number)
            if number == key_index:
                pre_text = colors['red']
            if answer == self.card.answer:
                pre_text = colors['green']
            print(pre_text + f'{letter}: {answer}' + colors['reset'])

        super().display()
        input('Press enter to continue.')


class NewCardPage(Page):
    def __init__(self, context, card_group):
        super().__init__(context)
        self.name = 'Card Creation'
        self.card_group = card_group

    def display(self):
        super().predisplay()

        group_adding_card_to = self.card_group

        new_card = Card(
            input('What is the question for this card?\n'),
            input('What is the answer for this card?\n')
        )

        user_input = input('What are some faux answers for this card? (ENTER to stop)\n')
        dummy_answers = []
        while user_input.lower() != '':
            dummy_answers.append(user_input)
            user_input = input('')

        new_card.dummy_answers = dummy_answers
        group_adding_card_to.cards.append(new_card)
        
        self.context.back()
        print('Completed card creation, press ENTER.')

    def parse_input(self, key):
        super().parse_input(key)


class EditCardPage(Page):
    def __init__(self, context, group, card_index):
            super().__init__(context)
            self.card = group.cards[card_index]
            self.name = 'Manage Cards'
            self.group = group
            self.card_index = card_index

    def display(self):
        super().predisplay()
        
        card = self.card

        print('Enter updated card question (ENTER to skip, X to delete)')
        print(f'CURRENT: {card.question}')
        new_question = input()
        if new_question.lower() == 'x':
            del self.group.cards[self.card_index]
            self.context.back()
            print('Card deleted press ENTER.')
            return
        card.question = new_question if new_question else card.question
        
        print('Enter updated answer')
        print(f'CURRENT: {card.answer}')
        new_answer = input()
        card.answer = new_answer if new_answer else card.answer
        
        print('Enter updated dummy answers')
        for index, dummy_answer in enumerate(card.dummy_answers):
            print(f'CURRENT: {dummy_answer}')
            new_dummy = input()
            card.dummy_answers[index] = new_dummy if new_dummy else dummy_answer
        
        print('Enter new dummy answers (Press ENTER when completed)')
        user_input = input()
        while user_input != '':
            card.dummy_answers.append(user_input)
            user_input = input()

        print('Completed editing card. Press ENTER')
        self.context.back()

    def parse_input(self, key):
        super().parse_input(key)


class ManageCardsPage(Page):
    def __init__(self, context, card_group):
        super().__init__(context)
        self.card_group = current_user.card_groups[card_group]
        self.name = 'Manage Cards'

    def display(self):
        super().predisplay()

        for index, card in enumerate(self.card_group.cards):
            print(f'{index}: {card.question}')

        print('\nn: New card')
        super().display(new_line=False)

    def parse_input(self, key):
        super().parse_input(key)

        if key in [str(x) for x in range(len(self.card_group.cards))]:
            self.context.add_page(EditCardPage(self.context,
                                               self.card_group,
                                               int(key)))
        
        elif key == 'n':
            self.context.add_page(NewCardPage(self.context,
                                              self.card_group))