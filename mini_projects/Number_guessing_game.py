import random
from random import *


def is_valid_interval(interval):
    if interval.isdigit():
        if 0 < int(interval) < 101:
            return True
        else:
            return False
    else:
        return False


def is_valid(num, interval):
    if num.isdigit():
        if 0 < int(num) < interval + 1:
            return True
        else:
            return False
    else:
        return False


def continue_game():
    print("Thanks for playing the number guessing game. One more time? (Yes/No)")
    answer = input().lower()

    while True:
        if answer == 'yes':
            return guessing_game()
        elif answer == 'no':
            print('Good luck. See you soon!')
            break
        else:
            print("A 'Yes' or 'No' response is accepted.")
            answer = input().lower()


def guessing_game():
    print("Welcome to number guessing game \n")
    print('Indicate in which range you are ready to guess the numbers\n(Between 1 and 100):\n')

    interval = input()

    while not is_valid_interval(interval):
        print("Interval must be a number between 1 and 100")
        interval = input()

    interval = int(interval)

    print("Enter a number from 1 to", interval)

    counter = 0
    num = input()
    x = randint(1, interval)

    while not is_valid(num, interval):
        print("Or maybe we'll just enter an integer from 1 to", interval, "?")
        num = input()

    num = int(num)

    while num != x:
        num = int(num)
        if num < x:
            counter += 1
            print("Your number is less than expected, please try again")
            num = input()
            while not is_valid(num, interval):
                print("Or maybe we'll just enter an integer from 1 to", interval, "?")
                num = input()
        elif num > x:
            counter += 1
            print("Your number is higher than expected, please try again")
            num = input()
            while not is_valid(num, interval):
                print("Or maybe we'll just enter an integer from 1 to", interval, "?")
                num = input()
        elif num == x:
            print("You guessed the hidden number in ", counter, "attempts, congratulations!")
            break

    print('♀ ' * 30)

    continue_game()


guessing_game()

# The program generates a random number between 1 and 100 and asks the user to guess the number.
# If the user's guess is greater than the random number, then the program should display the
# message 'Too much, try again'. If the guess is less than the random number, then the program
# should display the message 'Too small, try again'. If the user guesses the number, the program
# should congratulate him and display the message 'You guessed right, congratulations!'.
