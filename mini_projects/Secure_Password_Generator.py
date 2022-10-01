import random
from random import *

DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'
CHARS = ''


def is_valid_precondition(var):
        if not var.isdigit():
            return False
        else:
            return True


def is_answer_yes_or_no_valid(answer, symbols):
    global CHARS
    while True:
        if answer == 'yes':
            CHARS += symbols
            break
        elif answer == 'no':
            break
        else:
            answer = input("Please only answer 'Yes' or 'No'\n").lower()


def password_conditions():
    c = input("Whether to include the numbers 0123456789 in the password (Yes/No)\n").lower()
    is_answer_yes_or_no_valid(c, DIGITS)

    d = input("Whether to include uppercase letters ABCDEFGHIJKLMNOPQRSTUVWXYZ in the password (Yes/No)\n").lower()
    is_answer_yes_or_no_valid(d, UPPERCASE_LETTERS)

    e = input("Whether to include lowercase letters abcdefghijklmnopqrstuvwxyz in the password (Yes/No)\n").lower()
    is_answer_yes_or_no_valid(e, LOWERCASE_LETTERS)

    f = input("Whether to include characters !#$%&*+-=?@^_ in the password (Yes/No)\n").lower()
    is_answer_yes_or_no_valid(f, PUNCTUATION)

    g = input("Whether to exclude ambiguous characters il1Lo0O in the password (Yes/No)\n").lower()
    global CHARS
    while True:
        if g == 'no':
            CHARS += 'il1Lo0O'
            break
        elif g == 'yes':
            break
        else:
            g = input("Please only answer 'Yes' or 'No'\n").lower()


def generate_password(a, length):
    password = ''
    for i in range(int(a) + 1):
        print(password)
        password = ''
        for j in range(int(length)):
            password += choice(CHARS)


a = input("How many passwords should the program generate?\n")
while not is_valid_precondition(a):
    a = input("Please enter only numbers\n")


length = input("What is the password length?\n")
while not is_valid_precondition(length):
    length = input("Please enter only numbers\n")


password_conditions()
generate_password(a, length)
