from brain_games.cli import welcome_user


def run_game(description, game):
    name = welcome_user()
    print(description)
    i = 1
    while i <= 3:
        if not game():
            print("Let's try again, {}".format(name))
            return
        i += 1
    print("Congratulations, {}!".format(name))
    return
