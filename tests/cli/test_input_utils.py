from cli.input_utils import letter_to_peg, parse_input_to_pegs
from core.constants import ColorPeg


def test_letter_to_peg():
    result = letter_to_peg("Y")
    assert result == ColorPeg.YELLOW


def test_parse_input_to_pegs():
    guess_input = "R Y M G"
    expected = (ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.MAGENTA, ColorPeg.GREEN)

    result = parse_input_to_pegs(guess_input)

    assert result == expected
