s = input()
max_count = 0
b = 0

for i in range(len(s)):
    if s.count(s[i]) >= max_count:
        max_count = s.count(s[i])
        b = s[i]

print(b)

# The input is a string of text. The program displays the character that appears most often.
