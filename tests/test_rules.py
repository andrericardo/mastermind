from core.constants import ColorPeg
from core.rules import check_guess


def test_correct_guess_is_true():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = solution

    result = check_guess(solution, guess)

    assert result.is_winner


def test_incorrect_order_is_false():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = (ColorPeg.BLUE, ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.GREEN)

    result = check_guess(solution, guess)

    assert not result.is_winner


def test_incorrect_color_is_false():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = (ColorPeg.MAGENTA, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)

    result = check_guess(solution, guess)

    assert not result.is_winner


def test_colors_right_position_for_winner():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = solution

    result = check_guess(solution, guess)

    assert result.right_position == 4


def test_colors_wrong_position_for_winner():
    solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
    guess = solution

    result = check_guess(solution, guess)

    assert result.wrong_position == 0
