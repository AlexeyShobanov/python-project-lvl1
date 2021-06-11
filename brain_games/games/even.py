from random import randint
from brain_games.cli import check_answer
from brain_games.run_game import run_game


def isEven(number):
    return number % 2 == 0


def game_even():
    number = randint(1, 99)
    right_answer = "yes" if isEven(number) else "no"
    return check_answer(number, right_answer)


def run_game_even():
    description = 'Answer "yes" if the number is even, otherwise answer "no".'
    run_game(description, game_even)
    return
