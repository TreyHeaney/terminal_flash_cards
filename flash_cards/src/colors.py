colors = {
    'red': '\033[91m',
    'green': '\033[92m',
    'reset': '\033[0m',
}

def color_green(s):
    return colors['green'] + s + colors['reset']

def color_red(s):
    return colors['red'] + s + colors['reset']
