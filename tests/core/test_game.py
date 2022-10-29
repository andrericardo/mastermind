from core.constants import DEFAULT_ATTEMPTS, DEFAULT_PEGS_SIZE, ColorPeg
from core.game import get_colors_pegs, new_game


def swap_first_and_second_peg(pegs):
    return (pegs[1], pegs[0], *pegs[2:])


class TestGame:
    def test_get_colors_pegs(self):
        expected = (ColorPeg.RED, ColorPeg.BLUE, ColorPeg.YELLOW, ColorPeg.GREEN)
        result = get_colors_pegs(DEFAULT_PEGS_SIZE)
        assert result == expected

    def test_new_game(self):
        result = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)

        assert len(result.solution) == DEFAULT_PEGS_SIZE
        assert result.attempts_left == DEFAULT_ATTEMPTS

    def test_correct_guess(self):
        game = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)
        correct_guess = game.solution

        result = game.guess(correct_guess)

        assert game.attempts_left == DEFAULT_ATTEMPTS - 1
        assert result.last_guess.is_winner

    def test_incorrect_guess(self):
        game = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)
        incorrect_guess = swap_first_and_second_peg(game.solution)

        result = game.guess(incorrect_guess)

        assert game.attempts_left == DEFAULT_ATTEMPTS - 1
        assert not result.last_guess.is_winner

    def test_ran_out_of_attempts(self):
        game = new_game(DEFAULT_PEGS_SIZE, 1)
        incorrect_guess = swap_first_and_second_peg(game.solution)

        game.guess(incorrect_guess)
        game.guess(incorrect_guess)
        result = game.guess(incorrect_guess)

        assert game.attempts_left == 0
        assert not result.last_guess.is_winner
