s = input().split()
arr = []

for i in range(len(s)):
    for j in range(len(s[i])):
        if s[i][j] in '1234567890':
            arr.append(s[i][j])

print(''.join(arr))

# This code is equivalent to:

s = input().split()

arr = [s[i][j] for i in range(len(s)) for j in range(len(s[i])) if s[i][j] in '1234567890']

print(''.join(arr))