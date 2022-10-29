from core.constants import DEFAULT_ATTEMPTS, DEFAULT_PEGS_SIZE
from core.game import get_colors_pegs, new_game

from cli.formatter import format_pegs, format_result, format_title
from cli.input_utils import parse_input_to_pegs


def ask_guess():
    guess_input = input("Enter your guess:\n")
    return parse_input_to_pegs(guess_input)


def print_headers():
    print(format_title("Mastermind"))
    print("How to play")
    print(
        "Type the first letter of each color peg and press enter to submit your guess"
    )
    print('eg. "R B Y G" for (R)ed (B)lue (Y)ellow  (G)reen')
    print("The computer will tell you the number of color pegs in the right position")
    print("and the number of pegs of the correct color but on the wrong place.")


CHEAT = True


def main():
    print_headers()
    game = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)
    pegs_at_play = format_pegs(get_colors_pegs(DEFAULT_PEGS_SIZE))
    print(f"Pegs at play: {pegs_at_play}")

    if CHEAT:
        print(f"Solution: {format_pegs(game.solution)}")

    while not game.game_over:
        user_guess = ask_guess()
        guess_result = game.guess(user_guess)
        print(f"{format_pegs(user_guess)}{format_result(guess_result.last_guess)}")

        if game.game_over:
            if game.last_guess.is_winner:
                print("Congratulations whoo, whoo! you won!")

            yes_or_no = input("Play again? [Y/N]")
            if yes_or_no.lower() == "y":
                game = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)


if __name__ == "__main__":
    main()
