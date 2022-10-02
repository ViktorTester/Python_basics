a = input()
chars = list(a)
answer = 0

for i in range(len(chars)):
    chars[i] = int(chars[i])

for j in range(len(chars)):
    answer += (chars[j] * (2 ** (len(chars) - (j + 1))))

print(answer)