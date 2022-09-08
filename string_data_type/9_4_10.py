a = int(input())
counter = 0

for i in range(a):
    c = input()
    if c.count('11') >= 3:
        counter+= 1

print(counter)

# The first input is the number n - the number of messages,
# the next n lines contain strings containing latin lowercase letters and numbers.
# The program displays the number of lines that contain the number 11 at least 3 times.