n = int(input())
s = 0

while n > 0:
    if n % 2 == 0:
        s += n % 10
    n //= 10

print(s)

# A natural number is being processed.
# The program displays the sum of the even digits of this number,
# or 0 if there are no even digits in the entry.