n = int(input())

FACTORIAL_SUM = 0

for j in range(1, n + 1):
    TOTAL = 1
    for i in range(1, j + 1):
        TOTAL *= i
    FACTORIAL_SUM += TOTAL

print(FACTORIAL_SUM)

#  A natural number n is given. The program outputs the value of the sum 1! + 2! + 3! + ... + n!
