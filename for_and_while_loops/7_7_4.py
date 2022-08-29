mx = -10**6 - 1
s = 0
for i in range(10):
    x = int(input())
    if x < 0:
        s += x
    if x < 0 and x > mx:
        mx = x
if s < 0:
    print(s)
    print(mx)
else:
    print('NO')

# There is a sequence of 10 integers.
# It is known that the entered numbers do not exceed 10^6 in absolute value
# The program displays the sum of all negative numbers in the sequence
# and the maximum negative number in the sequence.
# If there are no negative numbers, "NO" is displayed.