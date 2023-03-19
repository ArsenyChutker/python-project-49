#!/usr/bin/env python3
import prompt
from random import randint
import random

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print ('What is the result of the expression?')
    win_count = 0
    while win_count < 3:
        win_count, our_answer, user_answer = play_round(win_count)
        if(win_count == -1):
            print (f""" '{user_answer}' is wrong answer ;(. Correct answer was '{our_answer}'.
Let's try again, {name}!""")
            break
    
    if(win_count == 3):
        print(f"""Congratulations, {name}""")
    return
    
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def play_round(win_count):
    num1 = (random.randint(0,100))
    num2 = (random.randint(0,100))
    operators = random.choice(["+","-","*"])
    num3 = f"{num1}{operators}{num2}"
    result = eval(num3)
    print (f'Question: {num3}')
    user_answer = prompt.string("Your answer: ")
    our_answer = str(result)
    if our_answer == user_answer:
        print ('Correct!')
        return win_count + 1, our_answer, user_answer
    else:
        return -1, our_answer, user_answer


if __name__ == '__main__':
    main()
