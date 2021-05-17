import platform

if platform.system() == 'Windows':
    clear_terminal = 'cls'
else:
    clear_terminal = 'clear'