'''Manages the page view stack.'''

from flash_cards.displays.welcome import WelcomePage
from flash_cards.displays.colors import colors

class PageContext:
    def __init__(self):
        self.page_stack = [WelcomePage(self)]
        self._message = ''

    def add_page(self, page):
        self.page_stack.append(page)

    def back(self):
        del self.page_stack[-1]

    @property
    def message(self):
        message = self._message
        self._message = ''
        return message
    
    @message.setter
    def message(self, message):
        color = colors['red']
        if 'success' in message: color = colors['green']

        self._message = color + message + colors['reset']


context = PageContext()
