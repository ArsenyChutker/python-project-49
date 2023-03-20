#!/usr/bin/env python3
import prompt
from random import randint
import random

def main():
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print ('Answer "yes" if given number is prime, Otherwise answer "no"')
    win_count = 0
    while win_count < 3:
        win_count = play_round(win_count)
        if(win_count == -1):
            print (f"""'yes' is wrong answer ;(. Correct answer was 'no'.
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
    random_number = (random.randint(0,100))
    print (f"Question: {random_number}")
    user_answer = prompt.string("Your answer: ")
    our_answer =  Prime_or_not(random_number)
    if our_answer == user_answer:
        print ('Correct!')
        return win_count + 1
    else:
        return -1

def checkPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
    

def Prime_or_not(num):
    if checkPrime(num):
        return "yes"
    else:
        return "no"

if __name__ == '__main__':
    main()

