class Page:
    def __init__(self, context):
        self.context = context
        self.name = 'page'

    def display(self, new_line=True):
        print(('\n' if new_line else '') + 'q: Quit, `: Back Page')

    def predisplay(self):
        print(' -> '.join([page.name for page in self.context.page_stack]) + '\n')

    def parse_input(self, key):
        if key == 'q':
            quit()
        elif key == '`':
            self.context.back()
