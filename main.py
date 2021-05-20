from flash_cards.cards.storage import load_save
from flash_cards.os_switches import clear_terminal
from flash_cards.context import context
import os
    
while True:
    os.system(clear_terminal)
    context.page_stack[-1].display()
    user_input = input()
    context.page_stack[-1].parse_input(user_input)