import random
from core.constants import DEFAULT_PEGS_SIZE, ColorPeg


def get_colors_pegs(number_of_pegs=DEFAULT_PEGS_SIZE):
    # TODO Assumes variant with no duplicates
    return tuple([ColorPeg(n) for n in range(1, number_of_pegs + 1)])
