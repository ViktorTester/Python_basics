n = x = int(input())
min_number = 9
max_number = -1

while x !=0:
    last_digit = x % 10
    x = x // 10
    if max_number < last_digit:
        max_number = last_digit

print("maximal number is", max_number)

while n !=0:
    last_digit = n % 10
    n = n // 10
    if min_number > last_digit:
        min_number = last_digit

print("minimal number is", min_number)

# The program determines the maximal and minimal digits of a number