#!/usr/bin/env python3

from brain_games.run_game import run_game
from brain_games.games.progression import game_progression


def main():
    description = 'What number is missing in the progression?'
    run_game(description, game_progression)


if __name__ == '__main__':
    main()
