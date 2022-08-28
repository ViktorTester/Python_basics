a = int(input())
flag = True
counter = 0

while a > 9:
    if a % 10 <= a // 10 % 10:
        flag = False
    else:
        flag = True
        counter += 1
    a = a // 10

if not flag and counter > 0:
    print("NO")
elif flag == True and counter > 0:
    print("NO")
elif not flag and counter == 0:
    print("YES")

# A natural number is given.
# The program determines whether the sequence of its digits,
# when viewed from left to right, is decreasing.