def get_middle_point(x1, y1, x2, y2):
    x = (x_1 + x_2) / 2
    y = (y_1 + y_2) / 2
    return x, y

x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)

# The get_middle_point(x1, y1, x2, y2) function takes as arguments the coordinates
# of the ends of the segment (x1, y1) and (x2, y2) and returns the coordinates
# of the point that is the middle of this segment.