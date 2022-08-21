x1, y1, x2, y2 = int(input()), int(input()), int(input()), int(input())
if (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print ('YES')
elif (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print ('YES')
else:
    print ('NO')

# The program determines whether the knight can get from the first cell to the second in one move.