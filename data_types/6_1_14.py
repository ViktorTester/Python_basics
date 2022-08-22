a = int(input())

num1 = a // 100
num2 = a % 100 // 10
num3 = a % 10

x = max(num1, num2, num3)
y = min(num1, num2, num3)
z = (num1 + num2 + num3) - x - y

if x - y == z:
    print("The number is interesting")
else:
    print("The number is not interesting")

# Let's call a number interesting if the difference between the maximum and minimum digit
# in it is equal to the average digit. The program determines an interesting number or not.
