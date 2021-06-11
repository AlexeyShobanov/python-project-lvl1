from random import randint
from brain_games.cli import check_answer


def get_random_operator(index):
    if index == 1:
        return '+'
    elif index == 2:
        return '-'
    return '*'


def calc_expression(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    return num1 * num2


def game_calc():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    operator = get_random_operator(randint(1, 3))
    right_answer = str(calc_expression(num1, num2, operator))
    question = "{} {} {}".format(num1, operator, num2)
    return check_answer(question, right_answer)
