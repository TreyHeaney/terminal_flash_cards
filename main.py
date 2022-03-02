from flash_cards.os_switches import clear_terminal
from flash_cards.context import context
import os

while True:
    os.system(clear_terminal)
    current_page = context.page_stack[-1]
    current_page.display()
    user_input = input()
    current_page.parse_input(user_input)
