num = int(input())
answer = ""

while num != 0:
    last_digit = num % 10
    answer = str(answer) + str(last_digit)
    num = num // 10

print(answer)

# The program reverses the order of the digits of a number