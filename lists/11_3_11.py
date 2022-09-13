n = int(input())
arr = []
total = 0

for i in range(n):
    a = int(input())
    total += a
    arr.append(total)
    total = a

print(arr[1:])

# The input to the program is a natural number n , and then n integers.
# The program creates a list from the specified numbers,
# consisting of the sums of neighboring numbers