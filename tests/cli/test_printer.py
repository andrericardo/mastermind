from cli.printer import format_peg, bcolors
from core.constants import ColorPeg


def test_format_peg():
    result = format_peg(ColorPeg.YELLOW)
    assert (
        result == f"{bcolors.BACKGROUND}{bcolors.YELLOW}Y {bcolors.ENDC}{bcolors.ENDC}"
    )
