from flash_cards.cards.storage import load_save
from flash_cards.os_switches import clear_terminal
from flash_cards.context import context
import os

c = load_save('./static/save.json')

while True:
    os.system(clear_terminal)
    # Do the same for color related things in cards.
    context.page_stack[-1].display()
    user_input = input()
    context.page_stack[-1].parse_input(user_input)