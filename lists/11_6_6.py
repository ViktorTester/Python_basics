a = input()
arr = a.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

x = max(arr)
y = min(arr)

for i in range(len(arr)):
  if arr[i] == x:
    arr[i] = y
  elif arr[i] == y:
    arr[i] = x

print(*arr)

# The input is a text string containing various natural numbers.
# A list of numbers is formed from this string.
# The program swaps the minimum and maximum element of this list.