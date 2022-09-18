s = input().split()
arr = []

for i in range(len(s)):
    s[i] = int(s[i])

for j in range(len(s)):
    if s[j] % 2 == 0 and s[j] ** 2 % 10 != 4:
        arr.append(s[j] ** 2)

print(*arr)

# This code is equivalent to:

s = input().split()

s = [int(s[i]) for i in range(len(s))]

# The input is a text string containing integers.
# The program displays the squares of even numbers that do not end with the number 4.

arr = [s[j] ** 2 for j in range(len(s)) if s[j] % 2 == 0 and s[j] ** 2 % 10 != 4]

print(*arr)