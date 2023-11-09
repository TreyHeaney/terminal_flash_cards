from flash_cards.src.page_template import Page

class SettingsPage(Page):
    def __init__(self, context):
        super().__init__(context)
        self.name = "Settings"
    
    def display(self):
        super().predisplay()

        super().display()

    def parse_input(self, key):
        super().parse_input(key)
