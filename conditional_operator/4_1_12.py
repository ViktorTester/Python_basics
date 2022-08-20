a, b, c = int(input()), int(input()), int(input())

positive = 0

if a >= 0:
    positive = positive + a

if b >= 0:
    positive = positive + b

if c >= 0:
    positive = positive + c

if positive == 0:
    print(0)
else:
    print(positive)

# A program that reads three numbers and only calculates the sum of positive numbers.