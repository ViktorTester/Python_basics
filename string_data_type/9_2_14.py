from math import floor, ceil

text = input()
half1 = ceil(len(text) / 2)
half2 = floor(len(text) / 2)

if len(text) == 1:
    print(text)
else:
    print((text[-half2:]) + (text[:half1]))

# The input is a single string.
# The program cuts it into two equal parts, rearranges them and displays them on the screen.