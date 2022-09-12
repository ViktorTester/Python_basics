from string import ascii_lowercase

n = int(input())
s = ascii_lowercase
print(list(s[:n]))

# or

n = int(input())
s = 'abcdefghijklmnopqrstuvwxyz'
print(list(s[:n]))

# or

c = ''
for i in range(98, int(input()) + 97):
    c += chr(i)
print(list(c))

# The input to the program is a single number n.
# The program outputs a list consisting of n letters of
# the English alphabet ['a', 'b', 'c', ...] in lower case.
