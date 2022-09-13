n = int(input())
arr = []

for i in range(n):
    a = input()
    arr.append(a)

k = int(input()) - 1

for j in range(n):
    if len(arr[j]) > k:
        print(arr[j][k], end='')

# The input to the program is a natural number n and n lines, and then the number k.
# The program prints the k-th letter from the input strings on one line without spaces.