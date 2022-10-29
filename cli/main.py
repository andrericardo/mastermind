from core.constants import DEFAULT_ATTEMPTS, DEFAULT_PEGS_SIZE
from core.game import new_game, get_colors_pegs
from printer import print_title, print_pegs, print_text


def ask_guess():
    print_text("> ")


def main():
    print_title("Mastermind")
    color_pegs = get_colors_pegs(DEFAULT_PEGS_SIZE)
    print_pegs(color_pegs)
    print_text("How to play")
    print_text(
        "Type the first letter of each color peg and press enter to submit your guess"
    )
    print_text('eg. "R Y B G" for (R)ed (Y)ellow (B)lue (G)reen')
    guess_input = input("Enter your guess: ")

    # game = new_game(DEFAULT_PEGS_SIZE, DEFAULT_ATTEMPTS)


if __name__ == "__main__":
    main()
