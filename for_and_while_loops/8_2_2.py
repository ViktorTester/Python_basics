n = 8
count = 0
maximum = -10 ** 12

for i in range(1, n + 1):
    x = int(input())
    if x % 4 == 0:
        count += 1
        if x > maximum:
            maximum = x

if count > 0:
    print(count)
    print(maximum)
else:
    print('NO')

# A sequence of 8 integers is received for processing.
# It is known that the entered numbers do not exceed 10 ** 12 in absolute value.
# The program displays the number of integer divisible by 4 numbers in the initial sequence,
# and the maximum divisible by 4 number. If there are no integers divisible by 4,
# you need to display "NO" on the screen.
