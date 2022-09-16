a = input()
arr = a.split()
counter = 0

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if arr[i] == arr[j]:
            counter +=1

print(counter)

# The input is a text string containing natural numbers. A list of numbers
# is formed from this string. The program counts how many pairs of elements
# in the resulting list are equal to each other. It is believed that any
# two elements that are equal to each other form one pair, which must be calculated.
