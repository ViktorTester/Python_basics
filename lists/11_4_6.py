n = int(input())
arr = []
arr2 = []

for i in range(n):
    a = z = input()
    a = a.lower()
    arr.append(a)
    arr2.append(z)

b = input()
b = b.lower()

for j in range(n):
    if b in arr[j]:
        print(arr2[j], sep='\n')

# The input is a natural number n, then n lines, then one more line — the search query.
# The program displays all the entered lines in which the search query occurs.