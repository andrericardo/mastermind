from core.constants import ColorPeg
from core.rules import GuessResult


class bcolors:
    RED = "\033[91m"
    BLUE = "\033[96m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    PURPLE = "\033[35m"

    RIGHT_POSITION = "\033[41m"
    WRONG_POSITION = "\033[100m"

    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"
    BACKGROUND = "\033[43m"


PEG_COLOR = {
    ColorPeg.RED: bcolors.RED,
    ColorPeg.BLUE: bcolors.BLUE,
    ColorPeg.YELLOW: bcolors.YELLOW,
    ColorPeg.GREEN: bcolors.GREEN,
    ColorPeg.MAGENTA: bcolors.MAGENTA,
    ColorPeg.PURPLE: bcolors.PURPLE,
}


def wrap_color(color):
    def wrapper(func):
        def wrapper_decorator(message):
            value = func(message)
            wrapped = f"{color}{value}{bcolors.ENDC}"
            return wrapped

        return wrapper_decorator

    return wrapper


@wrap_color(bcolors.BOLD)
@wrap_color(bcolors.RED)
@wrap_color(bcolors.UNDERLINE)
def format_title(message):
    return message


@wrap_color(bcolors.BACKGROUND)
def format_peg(peg: ColorPeg):
    letter = peg.name[0]
    color = PEG_COLOR[peg]
    return f"{color} {letter} {bcolors.ENDC}"


def format_pegs(pegs):
    return "".join([format_peg(p) for p in pegs])


@wrap_color(bcolors.BACKGROUND)
@wrap_color(bcolors.RIGHT_POSITION)
def right(message):
    return f"Right position: {message}"


@wrap_color(bcolors.BACKGROUND)
@wrap_color(bcolors.WRONG_POSITION)
def wrong(message):
    return f"Wrong position: {message}"


def format_result(result: GuessResult):
    return f" -> {right(result.right_position)} {wrong(result.wrong_position)}"


def format_attempts(attempts_left):
    return f"Attempts left: {attempts_left}"
