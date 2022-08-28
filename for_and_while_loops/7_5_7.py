a = b = c = int(input())
counter1 = 0
counter2 = 0
counter3 = 1

while a != 0:
    last_digit = a % 10
    a = a // 10
    counter1 += last_digit
    counter2 += 1
    counter3 *= last_digit

while b > 9:
    b = b // 10

last_digit = c % 10

print(counter1)
print(counter2)
print(counter3)
print(counter1 / counter2)
print(b)
print(last_digit + b)

# A natural number is given. The program calculates:
#
# the sum of its digits;
# the number of digits in it;
# the product of its digits;
# the average of its digits;
# its first digit;
# the sum of its first and last digits.