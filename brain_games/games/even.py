import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    win_count = 0
    while win_count < 3:
        win_count = play_round(win_count)
        if (win_count == -1):
            print(f"""'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, {name}!""")
            break

    if (win_count == 3):
        print(f"""Congratulations, {name}!""")
    return


def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def play_round(win_count):
    random_number = (random.randint(0, 100))
    print(f"Question: {random_number}")
    user_answer = prompt.string("Your answer: ")
    our_answer = checkEven(random_number)
    if our_answer == user_answer:
        print('Correct!')
        return win_count + 1
    else:
        return -1


def checkEven(num):
    if (num % 2 == 0):
        return "yes"
    else:
        return "no"
