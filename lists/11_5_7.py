a = input()
arr = a.split('.')
counter = 0

for i in range(len(arr)):
    arr[i] = int(arr[i])

for j in range(len(arr)):
    if 0 <= arr[j] <= 255:
        counter += 1

if counter == 4:
    print("YES")
else:
    print("NO")

# The input is a text string containing 4 integers separated by a dot.
# The program determines whether the entered text string is a valid ip-address.
