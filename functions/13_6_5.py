from math import *

def solve(a, b, c):
    x1 = 0
    x2 = 0

    D = pow(b, 2) - (4 * a * c)

    if D == 0:
        x1 = (-b / (2 * a))
        x2 = (-b / (2 * a))
    elif D > 0:
        x1 = ((-b + sqrt(D)) / (2 * a))
        x2 = ((-b - sqrt(D)) / (2 * a))

    if x1 < x2:
        return x1, x2
    else:
        return x2, x1


a, b, c = int(input()), int(input()), int(input())

x1, x2 = solve(a, b, c)
print(x1, x2)

# The solve(a, b, c) function takes as arguments three integers a, b, c - the coefficients
# of the quadratic equation ax ** 2 + bx + c = 0 and returns its roots in ascending order.
# It is guaranteed that the quadratic equation has roots.
