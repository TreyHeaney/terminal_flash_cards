class Page:
    def __init__(self, context):
        self.context = context
    
    def display(self):
        print('\nq: Quit, `: Back Page')

    def parse_input(self, key):
        if key == 'q':
            quit()
        elif key == '`':
            self.context.back()
