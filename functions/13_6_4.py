import math

def get_circle(radius):
    length = 2 * math.pi * r
    square = math.pi * ( r ** 2)
    return length, square

r = float(input())

length, square = get_circle(r)
print(length, square)

# The get_circle(radius) function takes the radius of a circle as an argument
# and returns two values: the length of the circle and the area
# of the circle enclosed by the given circle.