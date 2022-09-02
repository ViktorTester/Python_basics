a = int(input())

for i in range(1, a + 1):
    counter = 0
    for j in range(1, i + 1):
        if i % j == 0:
            counter += 1
    print(i, end='')
    print('+' * counter)

# The program displays a graphic representation of the divisibility of numbers from 1 to n.
# The new line displays the next number and as many "+" characters,
# as there are divisors for this number.