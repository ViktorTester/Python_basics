import random
from random import *

print("Hello World, I am a magic ball and I know the answer to any of your questions.\n")
print("What is your name? (I do not know this)")
name = input()

answers = ['Undoubtedly', 'I think yes', "It's still unclear", 'Try again', "Don't even think",
           "It's a foregone conclusion", 'Most likely', 'Ask later', 'My answer is no',
           'No doubt', 'Good prospects', 'Better not tell', 'According to my knowledge - no',
           'Definitely yes', 'Signs say yes', 'Now you can not predict',
           'Prospects are not very good', 'You can be sure of this', 'Yes',
           'Concentrate and ask again', 'Very doubtful']


def give_me_the_question():
    print("Ask your question", name )
    input()
    print(choice(answers))
    another_game()


def another_game():
    print("More questions? (Yes/ No)")
    reply = input().lower()
    while True:
        if reply == 'yes':
            return give_me_the_question()
        elif reply == 'no':
            print('Come back if you have any questions!')
            break
        else:
            print("'Yes' or 'No' accepted")
            reply = input().lower()


give_me_the_question()

# A magic ball (ball of fate) is a comic way to predict the future.
# The program should ask the user to ask a question in order to randomly answer it.