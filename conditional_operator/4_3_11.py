a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if a1 < b1 < a2 < b2 or a2 < b2 < a1 < b1:
    print("empty set")
elif a1 > a2 and b1 < b2:
    print(a1, b1)
elif a1 < a2 and b2 < b1:
    print(a2, b2)
elif a1 < a2 < b1 < b2:
    print(a2, b1)
elif a2 < a1 < b2 < b1:
    print(a1, b2)
elif a2 == b1:
    print(a2)
elif a1 == b2:
    print(a1)
elif a1 == a2 and b1 == b2:
    print(a1, b1)
elif (a1 == a2 and b1 < b2) or (b1 == b2 and a1 > a2):
    print(a1, b1)
elif (a1 == a2 and b1 > b2) or (b1 == b2 and a1 < a2):
    print(a2, b2)

# The number line has two segments: [a1; b1], [a2; b2]
# The program finds their intersection.
# The intersection of two segments can be:
#
# The program displays the boundaries of a segment that is an intersection,
# or a common point, or the text "empty set".
