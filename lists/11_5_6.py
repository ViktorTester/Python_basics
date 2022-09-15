a = input()
arr = a.split()

for i in range(len(arr)):
    arr[i] = int(arr[i])

for j in range(len(arr)):
    print(arr[j] * '+', end='\n')

# The input is a text string containing integers.
# The program builds a bar chart based on given numbers.
