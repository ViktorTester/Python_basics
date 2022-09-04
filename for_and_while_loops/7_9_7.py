a, b, = int(input()), int(input())

for i in range(a, b + 1):
    COUNT = 0
    for j in range(1, i + 1):
        if i % j == 0:
            COUNT += 1
    if COUNT == 2:
        print(i)

# The program receives two natural numbers a and b (a < b) as input.
# The program finds all prime numbers from a to b inclusive.
