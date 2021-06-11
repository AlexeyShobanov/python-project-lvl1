from random import randint
from brain_games.cli import check_answer
from brain_games.run_game import run_game


def isPrime(num):
    if num < 2:
        print(num % 2)
        return False
    i = 2
    while i <= num ** (0.5):
        if num % i == 0:
            return False
        i += 1
    return True


def game_prime():
    number = randint(1, 999)
    right_answer = "yes" if isPrime(number) else "no"
    return check_answer(number, right_answer)


def run_game_prime():
    description = 'Answer "yes" if given number is prime. ', \
        'Otherwise answer "no".'
    run_game(description, game_prime)
    return
