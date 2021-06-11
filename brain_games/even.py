import prompt
from random import randint


def isEven(number):
    return number % 2 == 0


def check_answer():
    number = randint(1, 99)
    rightAnswer = "yes" if isEven(number) else "no"
    answer = prompt.string("Question: {} \n".format(number))
    print("Your answer: {}".format(answer))
    result = answer == rightAnswer
    if result:
        print('Correct!')
    else:
        print(
            "\"{}\" is wrong answer ;(. Correct answer was \"{}\"."
            .format(answer, rightAnswer)
        )
    return result


def run_even_game(name):
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 1
    while i <= 3:
        if not check_answer():
            print("Let's try again, {}".format(name))
            return
        i += 1
    print("Congratulations, {}".format(name))
    return
