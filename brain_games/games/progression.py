from random import randint
from brain_games.cli import check_answer
from brain_games.run_game import run_game


def make_progression(base, increment, hiding_posission, progression_length):
    progression_stringify = ''
    i = 1
    while i < progression_length:
        current = base + increment * (i - 1)
        if i == hiding_posission:
            progression_stringify += '.. '
        else:
            progression_stringify += str(current) + ' '
        i += 1
    if hiding_posission == progression_length:
        progression_stringify += '..'
    else:
        progression_stringify += str(base +
                                     increment * (progression_length - 1))
    return progression_stringify


def game_progression():
    base = randint(1, 99)
    increment = randint(1, 99)
    progression_length = randint(5, 10)
    hiding_posission = randint(1, progression_length)
    progression_stringify = make_progression(
        base, increment, hiding_posission, progression_length)
    right_answer = str(base + increment * (hiding_posission - 1))
    question = "{}".format(progression_stringify)
    return check_answer(question, right_answer)


def run_game_progression():
    description = 'What number is missing in the progression?'
    run_game(description, game_progression)
    return
