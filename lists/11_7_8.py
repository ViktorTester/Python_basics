n = input()
n = n.split()
cube = []

for i in range(len(n)):
    n[i] = int(n[i])

for j in range(len(n)):
    cube.append(n[j] ** 3)

print(*cube)

# This code is equivalent to:

n = input().split()

n = [int(n[i]) for i in range(len(n))]

cube = [(n[j] ** 3) for j in range(len(n))]
print(*cube)

# The input is a text string containing integers.
# The program displays the cubes of the specified numbers also on one line.