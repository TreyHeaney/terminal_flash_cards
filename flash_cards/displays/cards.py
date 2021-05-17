'''Pages for viewing or managing cards.'''

import os
from random import choice, random, shuffle

from flash_cards.displays.page_template import Page


class ViewCardsPage(Page):
    def __init__(self, context, cards=[]):
        super().__init__(context)
        self.name = 'Viewing Cards'
        self.cards = cards

    def display(self):
        super().predisplay()

        random_card = choice(self.cards)
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

        if self.answers[key_index] == self.card.answer:
            pass

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
