#!/usr/bin/env python3

from brain_games.run_game import run_game
from brain_games.games.gcd import game_gcd


def main():
    description = 'Find the greatest common divisor of given numbers.'
    run_game(description, game_gcd)


if __name__ == '__main__':
    main()
