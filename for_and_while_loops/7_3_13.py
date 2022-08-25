n = int(input())

max1 = 0
max2 = 0

for i in range(n):
    num = int(input())
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2:
        max2 = num

print(max1)
print(max2)

# The input to the program is a natural number n,
# and then n different natural numbers,
# each on a separate line.
# The program outputs the largest and second-largest number in the sequence.