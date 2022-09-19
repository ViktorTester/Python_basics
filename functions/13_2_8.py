def draw_triangle(fill, base):
    for i in range(base):
        if i == (base / 2) + (1 / 2):
            break
        for j in range(i + 1):
            print(fill, end='')
        print()
    for i in range(int((base - ((base / 2) + (1 / 2))))):
        for j in range((int((base - ((base / 2) - (1 / 2))))), i + 1, -1):
            print(fill, end='')
        print()


fill = input()
base = int(input())

draw_triangle(fill, base)

# The draw_triangle(fill, base) function, which takes two parameters:

# fill - fill character;
# base - the value of the base of an isosceles triangle;
