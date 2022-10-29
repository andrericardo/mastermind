from cli.input_utils import letter_to_peg, parse_input_to_pegs
from core.constants import ColorPeg
import pytest


def test_letter_to_peg():
    result = letter_to_peg("Y")
    assert result == ColorPeg.YELLOW


@pytest.mark.parametrize("guess_input", ["R Y M G", "R y M g"])
def test_parse_input_to_pegs(guess_input):
    expected = (ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.MAGENTA, ColorPeg.GREEN)

    result = parse_input_to_pegs(guess_input)

    assert result == expected
