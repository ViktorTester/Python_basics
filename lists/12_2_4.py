a = input()
c = a.split('-')
b = a.replace('-', '')
arr = []
counter = 0

for i in range(len(b)):
    if b[i] in '1234567890':
        counter +=1

if counter == len(b):
    for j in range(len(c)):
        arr.append(len(c[j]))

if (arr == [1, 3, 3, 4] and a[0] == '7') or arr == [3, 3, 4]:
    print("YES")
else:
    print("NO")

# The input is a string of text. The program determines if the entered string
# is a valid phone number. A string of text is a valid phone number if it has
# the format: abc-def-hijk or 7-abc-def-hijk,
# where a, b, c, d, e, f, h, i, j, k are numbers from 0 to 9.