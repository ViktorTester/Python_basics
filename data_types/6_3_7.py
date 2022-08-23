from math import *

a, b, c = float(input()), float(input()), float(input())

x = 0
x1 = 0
x2 = 0

D = pow(b, 2) - (4 * a * c)

if D < 0:
    print("Нет корней")
elif D == 0:
    x = (-b / (2 * a))
elif D > 0:
    x1 = ((-b + sqrt(D)) / (2 * a))
    x2 = ((-b - sqrt(D)) / (2 * a))

if D == 0:
    print(x)
elif D > 0:
    print(min(x1, x2))
    print(max(x1, x2))

# Three real numbers a, b, c are given. The program finds the real roots of a quadratic equation