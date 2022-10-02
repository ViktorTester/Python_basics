a = input()
chars = list(a)
answer = 0

for i in range(len(chars)):
    if chars[i].isdigit():
        chars[i] = int(chars[i])
    elif chars[i] == 'A':
        chars[i] = 10
    elif chars[i] == 'B':
        chars[i] = 11
    elif chars[i] == 'C':
        chars[i] = 12
    elif chars[i] == 'D':
        chars[i] = 13
    elif chars[i] == 'E':
        chars[i] = 14
    elif chars[i] == 'F':
        chars[i] = 15

for j in range(len(chars)):
    answer += (chars[j] * (16 ** (len(chars) - (j + 1))))

print(answer)