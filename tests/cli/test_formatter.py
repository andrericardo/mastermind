from cli.formatter import (
    format_peg,
    format_result,
    Colors,
)
from core.constants import ColorPeg
from core.rules import GuessResult


def test_format_peg():
    result = format_peg(ColorPeg.YELLOW)
    assert result == f"{Colors.BACKGROUND}{Colors.YELLOW} Y {Colors.ENDC}{Colors.ENDC}"


def test_format_result():
    result = format_result(
        GuessResult(is_winner=False, right_position=2, wrong_position=1)
    )

    right = (
        f"{Colors.BACKGROUND}{Colors.RIGHT_POSITION}Right position: 2"
        f"{Colors.ENDC}{Colors.ENDC}"
    )
    wrong = (
        f"{Colors.BACKGROUND}{Colors.WRONG_POSITION}Wrong position: 1"
        f"{Colors.ENDC}{Colors.ENDC}"
    )

    expected = f" -> {right} {wrong}"

    assert result == expected
