from random import randint
from brain_games.cli import check_answer


def find_gcd(num1, num2):
    if num1 > num2:
        [num1, num2] = [num2, num1]
    while num1 != 0 and num2 != 0:
        [num1, num2] = [num2, num1 % num2]
    return num1


def game_gcd():
    num1 = randint(1, 99)
    num2 = randint(1, 99)
    right_answer = str(find_gcd(num1, num2))
    question = "{} {}".format(num1, num2)
    return check_answer(question, right_answer)
