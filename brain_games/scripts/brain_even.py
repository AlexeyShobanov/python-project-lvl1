#!/usr/bin/env python3

from brain_games.run_game import run_game
from brain_games.games.even import game_even


def main():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(description, game_even)


if __name__ == '__main__':
    main()
