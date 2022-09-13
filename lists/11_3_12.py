n = int(input())
arr = []

for i in range(n):
    a = int(input())
    arr.append(a)

del arr[1::2]

print(arr)

# The input is a natural number n, and then n integers.
# The program creates a list from the specified numbers,
# then removes all elements at odd indices, and then displays the resulting list.
