from core.constants import ColorPeg
from core.rules import check_guess


class TestCheckGuess:
    # It would be possible to combine these is_winner tests by using
    # @pytest.mark.parametrize but would make them harder to read
    def test_correct_guess_is_true(self):
        solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        guess = solution

        result = check_guess(solution, guess)

        assert result.is_winner

    def test_incorrect_order_is_false(self):
        solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        guess = (ColorPeg.BLUE, ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.GREEN)

        result = check_guess(solution, guess)

        assert not result.is_winner

    def test_incorrect_color_is_false(self):
        solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        guess = (ColorPeg.MAGENTA, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)

        result = check_guess(solution, guess)

        assert not result.is_winner

    def test_winner(self):
        solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        guess = solution

        result = check_guess(solution, guess)

        assert result.is_winner
        assert result.right_position == 4
        assert result.wrong_position == 0

    def test_position_swapped(self):
        solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        guess = (ColorPeg.BLUE, ColorPeg.RED, ColorPeg.YELLOW, ColorPeg.GREEN)

        result = check_guess(solution, guess)

        assert not result.is_winner
        assert result.right_position == 2
        assert result.wrong_position == 2

    def test_all_position_swapped(self):
        solution = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        guess = (ColorPeg.BLUE, ColorPeg.RED, ColorPeg.GREEN, ColorPeg.YELLOW)

        result = check_guess(solution, guess)

        assert not result.is_winner
        assert result.right_position == 0
        assert result.wrong_position == 4
