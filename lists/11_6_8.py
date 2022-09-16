a = input()
a = int(a[1::])
arr = []

for i in range(a):
    b = input()
    arr.append(b)

for j in range(len(arr)):
    if arr[j].find('#') > 0:
        arr[j] = arr[j][:arr[j].find('#')]
        arr[j] = arr[j].rstrip()

print(*arr, sep='\n')

# The first line contains a hash symbol and immediately a natural
# number n — the number of lines in the program, not counting the first one.
# This is followed by n lines of code.

# The program outputs the same lines, but removes comments
# and white space characters at the end of the lines.
