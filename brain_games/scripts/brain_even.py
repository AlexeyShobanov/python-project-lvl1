#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.even import run_even_game


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    run_even_game(name)


if __name__ == '__main__':
    main()
