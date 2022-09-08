a = input()
counter = 0

for i in range(len(a)):
    if a[i] != a[i].title():
        counter += 1

print(counter)

# The input is a string. The program counts the number of lowercase alphabetic characters.