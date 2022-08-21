cell = int(input())

if cell == 0:
    print("green")
elif (1 <= cell <= 10 or 19 <= cell <= 27) and (cell % 2 == 1):
    print("red")
elif (12 <= cell <= 18 or 30 <= cell <= 36) and (cell % 2 == 0):
    print("red")
elif (11 <= cell <= 17 or 29 <= cell <= 35) and (cell % 2 == 1):
    print("black")
elif (2 <= cell <= 10 or 20 <= cell <= 28) and (cell % 2 == 0):
    print("black")
else:
    print("Input Error")

# On the roulette wheel, the cells are numbered from 0 to 36. Below are the colors of the pockets:

# cell 0 is green;
# for cells from 1 to 10, odd-numbered pockets are red, even-numbered cells are black;
# for cells from 11 to 18, odd-numbered pockets are black, even-numbered cells are red;
# for cells 19 to 28, odd-numbered pockets are red, even-numbered cells are black;
# for cells 29 to 36, odd-numbered pockets are black, even-numbered pockets are red.

# The software reads the pocket number and shows if the pocket is green, red or black.
# The program displays an error message if the user enters a number that is outside the range of 0 to 36.