import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, {}!".format(name))
    return name


def check_answer(question, rightAnswer):
    answer = prompt.string("Question: {} \n".format(question))
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
