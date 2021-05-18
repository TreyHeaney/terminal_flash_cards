'''Pages for viewing or managing cards.'''

import os
import time
from random import choice, random, shuffle

from flash_cards.cards import Card
from flash_cards.cards.storage import groups
from flash_cards.cards.score_calculations import calculate_points, calculate_loss
from flash_cards.displays.page_template import Page


class ViewCardsPage(Page):
    '''View a single card and guess the answer.'''
    def __init__(self, context, cards=[]):
        super().__init__(context)
        self.name = 'Viewing Cards'
        self.cards = cards

    def display(self):
        super().predisplay()

        random_card = choice(self.cards)
        print(f'Card Strength: {random_card.score}')
        print(random_card.question + '\n')

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

        key_index = ord(key) - 97        
        if key_index not in [0, 1, 2, 3]:
            # Some sorta error would be preferrable here.
            return

        card = self.card
        if self.answers[key_index] == card.answer:
            time_since_correct = time.time() - card.last_correct
            card.score = calculate_points(time_since_correct,
                                          card.wrong_streak)

            card.wrong_streak = 0

            card.last_correct = time.time()
        else:
            card.score = calculate_loss(card.wrong_streak)

            card.wrong_streak += 1

        self.display_answer(key_index)

    def display_answer(self, key_index):
        os.system('clear')
        super().predisplay()

        print(self.card.question + '\n')

        for number, answer in enumerate(self.answers):
            pre_text = ''
            letter = chr(97 + number)
            if number == key_index:
                pre_text = '\033[91m'
            if answer == self.card.answer:
                pre_text = '\033[92m'
            print(pre_text + f'{letter}: {answer}' + '\033[0m')

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
        dummy_answers = [user_input]
        while user_input.lower() != '':
            user_input = input('')
            dummy_answers.append(user_input)

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
        self.card_group = groups[card_group]
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