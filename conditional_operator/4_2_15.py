a, b, c, d = int(input()), int(input()), int(input()), int(input())

x = a - c
y = b - d

if (x >=-1 and x <= 1) and (y >=-1 and y <= 1):
    print("YES")
else:
    print("NO")

# Two different cells of a chessboard are given.
# The program determines whether the King can get from the first cell to the second in one move.
# The program receives as input four numbers from 1 to 8 each, specifying the column number and row number,
# first for the first cell, then for the second cell.