from cli.input_utils import letter_to_peg, input_parser
from core.constants import ColorPeg


def test_letter_to_peg():
    result = letter_to_peg("Y")
    assert result == ColorPeg.YELLOW


def test_input_parser():
    guess_input = "R Y M G"
    expected = (ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.MAGENTA, ColorPeg.GREEN)

    result = input_parser(guess_input)

    assert result == expected
