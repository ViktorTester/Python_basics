a = int(input())
BIN = ""

while a != 0:
    BIN += str(a % 2)
    a = a // 2
for c in range(len(BIN), 0, -1):
    print(BIN[c - 1], end='')

# The input is a natural decimal number.
# The program converts the given number to the binary number system.