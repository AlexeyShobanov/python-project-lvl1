#!/usr/bin/env python3

from brain_games.run_game import run_game
from brain_games.games.calc import game_calc


def main():
    description = 'What is the result of the expression?'
    run_game(description, game_calc)


if __name__ == '__main__':
    main()
