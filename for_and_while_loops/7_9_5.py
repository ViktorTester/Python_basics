a = int(input())

while a > 9:
    counter = 0
    while a != 0:
        last_digit = a % 10
        counter += last_digit
        a = a // 10
    a = counter

print(a)

# The input to the program is a natural number.
# The program finds the digital root of the given number.
# The digital root of a number is obtained as follows: if you add all the digits of this number,
# then all the digits of the found sum and repeat this process,
# then the result will be a single-digit number (digit),
# which is called the digital root of this number.