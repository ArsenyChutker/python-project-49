#!/usr/bin/env python3
import prompt
from random import randint
import random

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print ('Find the greatest common divisor of given numbers.')
    win_count = 0
    while win_count < 3:
        win_count, our_answer, user_answer = play_round(win_count)
        if(win_count == -1):
            print (f""" '{user_answer}' is wrong answer ;(. Correct answer was '{our_answer}'.
Let's try again, {name}!""")
            break
    
    if(win_count == 3):
        print(f"""Congratulations, {name}!""")
    return
    
def welcome_user():
    name = prompt.string('May I have your name? ')
    print(f"Hello, {name}!")
    return name


def play_round(win_count):
    a = (random.randint(0,100))
    b = (random.randint(0,100))
    while a!=b:
        if a > b:
            a -= b
        else:
            b -= a
    our_answer = b
    print (f'Question:{a} {b}')
    user_answer = int(prompt.string("Your answer: "))
    if our_answer == user_answer:
        print ('Correct!')
        return win_count + 1, our_answer, user_answer
    else:
        return -1, our_answer, user_answer



if __name__ == '__main__':
    main()
