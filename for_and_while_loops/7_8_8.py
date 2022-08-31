n = int(input())

for i in range(1, n + 1):
    for j in range(i):
        if i + j <= n:
            print('*', end='')
    print()

# An odd natural number n is given. The program prints an isosceles star triangle with base n.