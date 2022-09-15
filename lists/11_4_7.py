n = int(input())
arr = []
arr2 = []
counter = 0

for i in range(n):
    a = input()
    arr.append(a)

k = int(input())

for j in range(k):
    b = input()
    arr2.append(b)

for y in range(n):
    counter = 0
    for x in range(k):
        if arr2[x].lower() in arr[y].lower():
            counter += 1
        if counter == k:
            print(arr[y])
            counter = 0

# The input is a natural number n, then n strings, then the number k — the number
# of search queries, then k strings — search queries. The program displays all the
# entered lines in which all search queries occur.