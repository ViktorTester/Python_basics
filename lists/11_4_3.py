n = int(input())
arr = []

for i in range(n):
    x = int(input())
    print(x)
    arr.append(x)

print()

for j in arr:
    print((j ** 2) + (2 * j) + 1)

# The input is a natural number n, and then n integers.
# The program, for each entered number x displays the value of the function f(x) = x^2 + 2x + 1