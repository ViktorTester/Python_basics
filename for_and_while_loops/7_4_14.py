num = int(input())
counter = 0

while num >= 25:
    counter += 1
    num = num - 25

while num >= 10:
    counter += 1
    num = num - 10

while num >= 5:
    counter += 1
    num = num - 5

while num >= 1:
    counter += 1
    num = num - 1

print(counter)

# There are banknotes with denominations: 1, 5, 10, 25.
# The input is one number (price for the service).
# The program shows the minimum number of banknotes required to pay for the service.