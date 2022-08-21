a, b, c, d = int(input()), int(input()), int(input()), int(input())
if b == d or a == c or abs(a - c) == abs(b - d):
    print("YES")
else:
    print("NO")

# The program determines whether the queen can get from the first cell to the second in one move.