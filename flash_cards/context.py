'''Manages the page view stack.'''

from flash_cards.displays.welcome import WelcomePage


class PageContext:
    def __init__(self):
        self.page_stack = [WelcomePage(self)]

    def add_page(self, page):
        self.page_stack.append(page)

    def back(self):
        del self.page_stack[-1]

context = PageContext()
