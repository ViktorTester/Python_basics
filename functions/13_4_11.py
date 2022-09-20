def merge(list1, list2):
    numbers1.extend(numbers2)

    n = len(numbers1)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if numbers1[j] > numbers1[j + 1]:
                numbers1[j], numbers1[j + 1] = numbers1[j + 1], numbers1[j]
    return numbers1

numbers1 = [int(c) for c in input().split()]
numbers2 = [int(c) for c in input().split()]

print(merge(numbers1, numbers2))

# The merge(list1, list2) function takes two ascending sorted lists
# of integers as arguments and merges them into a single sorted list.