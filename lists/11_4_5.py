n = int(input())
arr = []

for i in range(n):
    a = input()
    if a not in arr:
        arr.append(a)

print(*arr, sep='\n')

# The input is a natural number n, and then n strings.
# The program outputs only unique strings, in the same order in which they were entered.