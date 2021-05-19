'''OS related pivots for multi-OS support.'''

import platform

if platform.system() == 'Windows':
    clear_terminal = 'cls'
else:
    clear_terminal = 'clear'