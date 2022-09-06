a = input()
counter = 0

for c in range(len(a) - 1):
    if a[c] == a[c + 1]:
        counter += 1

print(counter)

# The input is a single string.
# The program determines how many identical neighboring characters are in it.
