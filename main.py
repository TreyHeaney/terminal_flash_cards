from flash_cards.context import context
import os

while True:
    os.system('clear')  # Offload this to deal with OS differences.
    context.page_stack[-1].display()
    user_input = input()
    context.page_stack[-1].parse_input(user_input)