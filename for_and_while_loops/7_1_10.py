m, p, n = int(input()), int(input()), int(input())

x = ((p / 100) + 1)

print("1", m)

for i in range(n - 1):
    m = m * x
    print(i + 2, m)

# The program predicts the size of an organism's population.
# m - the initial number of organisms;
# p - average daily increase in %;
# n - the number of days for reproduction.