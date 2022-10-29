from dataclasses import dataclass
import random
from core.constants import ColorPeg
from core.rules import check_guess


@dataclass
class Game:
    solution: tuple
    attempts_left: int
    last_guess: tuple = None
    game_over: bool = False

    def guess(self, guessed_pegs):
        if self.attempts_left > 0:
            self.attempts_left -= 1
            self.last_guess = check_guess(self.solution, guessed_pegs)

        if not self.last_guess.is_winner and self.attempts_left == 0:
            self.game_over = True

        return self


def get_colors_pegs(number_of_pegs):
    # TODO Assumes variant with no duplicates
    return tuple([ColorPeg(n) for n in range(1, number_of_pegs + 1)])


def shuffle_pegs(pegs):
    pegs_as_list = list(pegs)
    random.shuffle(pegs_as_list)
    return tuple(pegs_as_list)


def new_game(number_of_pegs, attempts_left):
    color_pegs = get_colors_pegs(number_of_pegs)
    shuffled_pegs = shuffle_pegs(color_pegs)
    return Game(solution=shuffled_pegs, attempts_left=attempts_left)
