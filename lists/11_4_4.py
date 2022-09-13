n = int(input())
arr = []
arr2 = []

for i in range(n):
    s = int(input())
    arr.append(s)

for j in range(n):
    if arr[j] != max(arr) and arr[j] != min(arr):
        arr2.append(arr[j])

print(*arr2, sep='\n')

# The input is a natural number n, and then n different natural numbers.
# The program removes the smallest and largest value from the specified numbers,
# and then prints the remaining numbers each on a separate line, without changing their order.