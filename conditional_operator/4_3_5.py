a, b, c = int(input()), int(input()), int(input())

if a < b < c or a > b > c or c < b < a or c > b > a:
    print(b)
elif b > a > c or b < a < c or c > a > b or c < a < b:
    print(a)
else:
    print(c)

# A program that finds the average of three numbers.
