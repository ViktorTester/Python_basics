n = int(input())
max_digit = -1

while n != 0:
    last_digit = n % 10
    if last_digit % 3 == 0:
        if max_digit < last_digit:
            max_digit = last_digit
    n = n // 10

if not max_digit % 3 == 0:
    print('NO')
else:
    print(max_digit)

# A natural number is being processed.
# The program displays the maximum digit of a number that is a multiple of 3.
# If there are no digits divisible by 3 in the number, “NO” is displayed on the screen.