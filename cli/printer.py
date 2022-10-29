from core.constants import ColorPeg


class bcolors:
    RED = "\033[91m"
    BLUE = "\033[96m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    PURPLE = "\033[35m"

    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BACKGROUND = "\033[43m"


PEG_COLOR = {
    ColorPeg.RED: bcolors.RED,
    ColorPeg.BLUE: bcolors.BLUE,
    ColorPeg.YELLOW: bcolors.YELLOW,
    ColorPeg.GREEN: bcolors.MAGENTA,
    ColorPeg.MAGENTA: bcolors.MAGENTA,
    ColorPeg.PURPLE: bcolors.PURPLE,
}


def color_print(color):
    def wrapper(func):
        def wrapper_decorator(message):
            message = f"{color}{message}{bcolors.ENDC}"
            value = func(message)
            return value

        return wrapper_decorator

    return wrapper


def wrap_color(color):
    def wrapper(func):
        def wrapper_decorator(message):
            value = func(message)
            wrapped = f"{color}{value}{bcolors.ENDC}"
            return wrapped

        return wrapper_decorator

    return wrapper


@color_print(bcolors.BOLD)
@color_print(bcolors.RED)
@color_print(bcolors.UNDERLINE)
def print_title(message):
    print(message)


def print_text(message):
    print(message)


def print_pegs(pegs):
    print(format_pegs(pegs))


@wrap_color(bcolors.BACKGROUND)
def format_peg(peg: ColorPeg):
    letter = peg.name[0]
    color = PEG_COLOR[peg]
    return f"{color}{letter} {bcolors.ENDC}"


def format_pegs(pegs):
    return "".join([format_peg(p) for p in pegs])
