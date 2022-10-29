from enum import Enum, unique


@unique
class ColorPeg(Enum):
    RED = 1
    BLUE = 2
    YELLOW = 3
    GREEN = 4
    MAGENTA = 5
    PURPLE = 6


DEFAULT_PEGS_SIZE = 4
