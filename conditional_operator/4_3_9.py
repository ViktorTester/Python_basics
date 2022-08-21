c1, c2 = input(), input()
r, b, y = "red", "blue", "yellow"

if (c1 == r and c2 == b) or (c1 == b and c2 == r):
    print("violet")
elif (c1 == r and c2 == y) or (c1 == y and c2 == r):
    print("orange")
elif (c1 == y and c2 == b) or (c1 == b and c2 == y):
    print("green")
elif c1 == r and c2 == r:
    print("red")
elif c1 == b and c2 == b:
    print("blue")
elif c1 == y and c2 == y:
    print("yellow")
else:
    print("color mistake")

# A program that reads the names of two primary colors to mix.
# If the user enters anything other than the names "red", "blue" or "yellow",
# then the program should display an error message. Otherwise,
# the program should display the name of the secondary color that will be the result.
