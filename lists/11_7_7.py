n = int(input())
square = []
for i in range(1, n + 1):
    square.append(i ** 2)
print(*square, sep='\n')

# This code is equivalent to:

square = [(i ** 2) for i in range(1, n + 1)]
print(*square, sep='\n')

# The input is a natural number n. The program creates a list containing
# the squares of numbers from 1 to n, and then displays its
# elements line by line, that is, each on a separate line.