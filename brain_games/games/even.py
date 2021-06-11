from random import randint
from brain_games.cli import check_answer


def isEven(number):
    return number % 2 == 0


def game_even():
    number = randint(1, 99)
    right_answer = "yes" if isEven(number) else "no"
    return check_answer(number, right_answer)
