n = int(input())

for i in range(2, n + 1):
    if n % i == 0:
        break

print(i)

# The input to the program is a number n > 1.
# The program outputs its smallest divisor other than 1.