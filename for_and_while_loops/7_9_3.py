a= int(input()), int(input())
dividers_count = 0
max_divider = 0
for i in range(a, b + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += j
        if count >= dividers_count:
            dividers_count = count
            max_divider = i
print(max_divider, dividers_count, sep=' ')


# The input to the program is two natural numbers.
# The program displays: the number with the maximum sum of divisors
# and the sum of its divisors.