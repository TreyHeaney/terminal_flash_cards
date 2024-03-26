'''Pages for viewing or managing cards.'''

import os
import random
import time
from collections import deque
from random import choices, shuffle

from flash_cards.cards import Card, draw_card
from flash_cards.accounts import current_user
from flash_cards.os_switches import clear_terminal
from flash_cards.storage.card_storage import save
from flash_cards.src.colors import colors, color_red, color_green
from flash_cards.src.page_template import Page
from flash_cards.src.score_calculations import calculate_points, calculate_loss
from flash_cards.src.strings.basics import newline
from flash_cards.src.strings.cards import CardStrings
from flash_cards.src.strings.prompts import PromptStrings

alphabet_start_ord = 97


class ViewCardsPage(Page):
    '''View a single card and guess the answer.'''
    def __init__(self, context, cards=[]):
        super().__init__(context)
        self.name = 'Viewing Cards'
        self.cards = cards

        scaled_max = int(len(self.cards) * 0.33)
        low_max = len(self.cards) - 2
        max_history = min(low_max, scaled_max)

        self.redraw = True
        self.recently_drawn = deque([], maxlen=max_history)
        self.last_correct = True

    def display(self):
        super().predisplay()
        if self.redraw:
            card = draw_card(self.cards, 
                             self.recently_drawn,
                             draw_strong=not self.last_correct)

            self.recently_drawn.append(card)

            self.last_score = card.score
            shuffle(card.dummy_answers)
            self.choices = card.dummy_answers[:3] + [card.answer]
            shuffle(self.choices)
            self.card = card
        else:
            self.redraw = True

        print(f'Card score: {self.card.score}')
        print(self.card.question + newline)
        for i, choice in enumerate(self.choices):
            letter = chr(alphabet_start_ord + i)
            print(f'{letter}: {choice}')

        super().display()

    def incorrect_input(self):
        self.redraw = False
        self.context.message = 'Invalid input!'

    def parse_input(self, key):
        super().parse_input(key)

        if len(key) != 1: 
            self.incorrect_input()
            return
        key_index = ord(key) - alphabet_start_ord
        out_of_range = key_index not in [x for x in range(len(self.choices))]
        if out_of_range: 
            self.incorrect_input()
            return
        card = self.card
        answer_is_correct = self.choices[key_index] == card.answer
        if answer_is_correct:
            time_since_correct = time.time() - card.last_correct
            card.score += calculate_points(time_since_correct,
                                           card.wrong_streak)
            card.score = min((10, card.score))
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

        print(f'Score change: {self.last_score} -> {self.card.score}')
        print(self.card.question + newline)

        for number, choice in enumerate(self.choices):
            letter = chr(alphabet_start_ord + number)
            s = f'{letter}: {choice}'
            if choice == self.card.answer:
                s = color_green(s)
            elif number == key_index:
                s = color_red(s)
            print(s)

        super().display()
        input(PromptStrings.press_enter)


class NewCardPage(Page):
    def __init__(self, context, card_group):
        super().__init__(context)
        self.name = 'Card Creation'
        self.card_group = card_group

    def display(self):
        super().predisplay()

        new_card = Card(
            input(PromptStrings.cards.get_question),
            input(PromptStrings.cards.get_answer)
        )

        user_input = input(PromptStrings.cards.faux_answer)
        dummy_answers = []
        while user_input.lower() != '':
            dummy_answers.append(user_input)
            user_input = input('')

        new_card.dummy_answers = dummy_answers
        self.card_group.cards.append(new_card)
        
        self.context.back()
        print(PromptStrings.press_enter)
        save(current_user.card_groups, 
             current_user.settings['save_location'])

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
        print(CardStrings.f_display_current(card.question))
        new_question = input()
        if new_question.lower() == 'x':
            del self.group.cards[self.card_index]
            self.context.back()
            print('Card deleted. ' + PromptStrings.press_enter)
            return
        card.question = new_question if new_question else card.question
        
        print('Enter updated answer')
        print(CardStrings.f_display_current(card.answer))
        new_answer = input()
        card.answer = new_answer if new_answer else card.answer
        
        print('Enter updated dummy answers')
        for index, dummy_answer in enumerate(card.dummy_answers):
            print(CardPrompts.f_display_current(dummy_answer))
            new_dummy = input()
            card.dummy_answers[index] = new_dummy if new_dummy else dummy_answer
        
        print('Enter new dummy answers (Press ENTER when completed)')
        user_input = input()
        while user_input != '':
            card.dummy_answers.append(user_input)
            user_input = input()

        print('Completed editing card. ' + PromptStrings.press_enter)
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

        print(newline + 'n: New card')
        super().display(linebreak=False)

    def parse_input(self, key):
        super().parse_input(key)

        if key in [str(x) for x in range(len(self.card_group.cards))]:
            self.context.add_page(EditCardPage(self.context,
                                               self.card_group,
                                               int(key)))
        
        elif key == 'n':
            self.context.add_page(NewCardPage(self.context,
                                              self.card_group))