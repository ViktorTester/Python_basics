a = input()
flag = True

for i in range(len(a)):
    if a[i] in '0123456789':
        flag = False
        break

if flag:
    print("The string does not contain digits")
else:
    print("The string contains numbers")

# The input to the program is a single string. The program checks if the string contains a digit.
