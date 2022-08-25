total = 0

for i in range(1, 11):
    num = int(input())
    total += num

if total % 2 == 0 and num * num % 2 == 0:
    print("YES")
else:
    print("NO")

# The program reads a sequence of 10 integers and determines whether each of them is even or not.