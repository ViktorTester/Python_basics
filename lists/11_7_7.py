n = int(input())
square = []
for i in range(1, n + 1):
    square.append(i ** 2)
print(*square, sep='\n')

# This code is equivalent to:

square = [(i ** 2) for i in range(1, n + 1)]
print(*square, sep='\n')