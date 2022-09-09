s = input()
counter = 0

for i in range(len(s)):
    if s[i] in '1234567890':
        counter +=1

print(counter)

# The input is a string of text. The program counts the number of digits in a given string.