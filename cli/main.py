from core.constants import DEFAULT_ATTEMPTS, DEFAULT_PEGS_SIZE
from core.game import get_colors_pegs, new_game

from cli.formatter import format_attempts, format_pegs, format_result, format_title
from cli.input_utils import parse_input_to_pegs


def print_headers():
    print(format_title("Mastermind"))
    print("How to play")
    print(
        "Type the first letter of each color peg and press enter to submit your guess"
    )
    print('eg. "R B Y G" for (R)ed (B)lue (Y)ellow  (G)reen')
    print("The computer will tell you the number of color pegs in the right position")
    print("and the number of pegs of the correct color but on the wrong place.")


def ask_guess():
    guess_input = input("Enter your guess:\n")
    return parse_input_to_pegs(guess_input)


def game_loop():
    game = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)
    pegs_at_play = format_pegs(get_colors_pegs(DEFAULT_PEGS_SIZE))
    print(f"Pegs at play: {pegs_at_play}")

    if True:
        print(format_pegs(game.solution))

    while not game.game_over:
        user_guess = ask_guess()
        if len(user_guess) < DEFAULT_PEGS_SIZE:
            continue
        guess_result = game.guess(user_guess)

        formatted_result = (
            f"{format_pegs(user_guess)}"
            f"{format_result(guess_result.last_guess)} "
            f"{format_attempts(game.attempts_left)}"
        )
        print(formatted_result)

        if game.game_over:
            if game.last_guess.is_winner:
                print("Congratulations whoo, whoo! You won!")
            else:
                print("Too bad, you lost!")

            yes_or_no = input("Play again? [y/N]")
            if yes_or_no.lower() == "y":
                game_loop()


def main():
    print_headers()
    game_loop()


if __name__ == "__main__":
    main()
