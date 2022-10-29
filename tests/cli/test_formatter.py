from cli.formatter import (
    format_peg,
    format_result,
    bcolors,
)
from core.constants import ColorPeg
from core.rules import GuessResult


def test_format_peg():
    result = format_peg(ColorPeg.YELLOW)
    assert (
        result == f"{bcolors.BACKGROUND}{bcolors.YELLOW} Y {bcolors.ENDC}{bcolors.ENDC}"
    )


def test_format_result():
    result = format_result(
        GuessResult(is_winner=False, right_position=2, wrong_position=1)
    )

    right = (
        f"{bcolors.BACKGROUND}{bcolors.RIGHT_POSITION}Right position: 2"
        f"{bcolors.ENDC}{bcolors.ENDC}"
    )
    wrong = (
        f"{bcolors.BACKGROUND}{bcolors.WRONG_POSITION}Wrong position: 1"
        f"{bcolors.ENDC}{bcolors.ENDC}"
    )

    expected = f" -> {right} {wrong}"

    assert result == expected
