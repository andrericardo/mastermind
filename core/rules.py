from dataclasses import dataclass


@dataclass
class GuessResult:
    is_winner: bool
    right_position: int
    wrong_position: int


def check_guess(solution, guess) -> GuessResult:
    right_position = 0
    wrong_position = 0

    for (solution_peg, guess_peg) in zip(solution, guess):
        if solution_peg == guess_peg:
            right_position += 1
        elif guess_peg in solution:
            wrong_position += 1

    is_winner = right_position == len(guess)

    return GuessResult(is_winner, right_position, wrong_position)
