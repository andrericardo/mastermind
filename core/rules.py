from dataclasses import dataclass


@dataclass
class GuessResult:
    is_winner: bool
    right_position: int
    wrong_position: int


def check_guess(solution, guess) -> GuessResult:
    is_winner = solution == guess
    right_position = len(guess)
    wrong_position = 0
    return GuessResult(is_winner, right_position, wrong_position)
