a, b = input().split(), input().split()
arr = []

for i in range(len(a)):
    a[i] = int(a[i])

for j in range(len(b)):
    b[j] = int(b[j])

for x in range(len(a)):
    arr.append(b[x] + a[x])

print(*arr)

# The input to the program is two lines of text containing integers.
# Lists of numbers are formed from these strings. The program creates a
# third list whose elements are the sums of the corresponding elements
# of the first two lists. Next, the program should display
# each element of the resulting list on one line.