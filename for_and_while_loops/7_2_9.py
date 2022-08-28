m, n = int(input()), int(input())

if m % 2 == 0:
    for i in range(m - 1, n - 1, -2):
        print(i)
elif m % 2 == 1:
    for i in range(m, n - 1, -2):
        print(i)

# same without if:

m, n = int(input()), int(input())

m = m % 2 + m - 1

for i in range(m, n - 1, -2):
    print(i)

# Two integers m and n (m > nm > n) are given.
# The program displays all odd numbers from m to n inclusive in descending order.