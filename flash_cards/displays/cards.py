from flash_cards.displays.page_template import Page

class ViewCardsPage(Page):
    def __init__(self, context):
        super().__init__(context)

    def parse_input(self, key):
        super().parse_input(key)