n = int(input())

a = b = 1

if n == 1:
    print(1)
else:
    print(a, b, end=' ')

for i in range(2, n):
    a, b = b, a + b
    print(b, end=' ')

# The program reads a natural number n and prints the first n numbers of the Fibonacci sequence.