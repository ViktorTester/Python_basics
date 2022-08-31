n = int(input())

for i in range(1, n + 1):
    for j in range(1, 10):
        print(i, '+', j, '=', i + j)
    print()

# Given a natural number n (n <= 9).
# The program prints the addition table starting from 1 + 1 to 9, and ending with n + 1 to 9