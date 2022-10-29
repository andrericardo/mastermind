from core.constants import ColorPeg


# Assumes color names have unique starting letters
def letter_to_peg(letter: str):
    return next(peg for peg in ColorPeg if peg.name[0] == letter)


def input_parser(guess_input: str):
    each_letter = guess_input.strip().split(" ")
    return tuple([letter_to_peg(letter) for letter in each_letter])
