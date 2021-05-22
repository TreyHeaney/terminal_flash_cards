from flash_cards.os_switches import clear_terminal
from flash_cards.context import context
import os

# Really this is the jist of it. This runs on a loop until the program is ended.
while True:
    os.system(clear_terminal)
    context.page_stack[-1].display()
    user_input = input()
    context.page_stack[-1].parse_input(user_input)
