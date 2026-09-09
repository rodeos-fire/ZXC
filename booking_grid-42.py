# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: BookingGrid
ANSI = {
    'reset':     '\033[0m',
    'bold':      '\033[1m',
    'dim':       '\033[2m',
    'red':       '\033[31m',
    'green':     '\033[32m',
    'yellow':    '\033[33m',
    'blue':      '\033[34m',
    'magenta':   '\033[35m',
    'cyan':      '\033[36m',
    'white':     '\033[37m',
    'bright_red': '\033[91m',
    'bright_green': '\033[92m',
    'bright_yellow': '\033[93m',
    'bright_blue': '\033[94m',
    'bright_magenta': '\033[95m',
    'bright_cyan': '\033[96m',
    'bright_white': '\033[97m',
    'bg_red':    '\033[41m',
    'bg_green':  '\033[42m',
    'bg_yellow': '\033[43m',
    'bg_blue':   '\033[44m',
    'bg_magenta': '\033[45m',
    'bg_cyan':   '\033[46m',
    'bg_white':  '\033[47m',
}

def _colorize(text, color):
    return f"{ANSI[color]}{text}{ANSI['reset']}" if color else text

def _print_color(text, color):
    print(_colorize(text, color))

def _print_section(title):
    print(f"\n{_print_color(f'=== {title} ===', 'bright_cyan')}")

def _print_row(*cells):
    print(' | '.join(_colorize(c, 'cyan') if i % 2 == 0 else c for i, c in enumerate(cells)))

def _print_success(msg):
    print(f"{ANSI['green']}✓ {msg}{ANSI['reset']}")

def _print_error(msg):
    print(f"{ANSI['red']}✗ {msg}{ANSI['reset']}")

def _print_warning(msg):
    print(f"{ANSI['yellow']}⚠ {msg}{ANSI['reset']}")

def _print_info(msg):
    print(f"{ANSI['blue']}ℹ {msg}{ANSI['reset']}")
