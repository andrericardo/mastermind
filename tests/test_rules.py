from core.constants import ColorPeg
from core.rules import check_guess


def test_correct_guess_is_true():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = solution

    result = check_guess(solution, guess)

    assert result


def test_incorrect_order_is_false():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = (ColorPeg.BLUE, ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.GREEN)

    result = check_guess(solution, guess)

    assert not result


def test_incorrect_color_is_false():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = (ColorPeg.MAGENTA, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)

    result = check_guess(solution, guess)

    assert not result
