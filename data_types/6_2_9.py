a, b, c = input(), input(), input()

most_min = 0
most_max = 0

l1 = len(a)
l2 = len(b)
l3 = len(c)

l_min = min(l1, l2, l3)
l_max = max(l1, l2, l3)
l_avg = (l1 + l2 + l3) - (l_min + l_max)

if l1 == l_min:
    most_min = most_min + l1
elif l2 == l_min:
    most_min = most_min + l2
elif l2 == l_min:
    most_min = most_min + l3

if l1 == l_max:
    most_max = most_max + l1
elif l2 == l_max:
    most_max = most_max + l1
elif l2 == l_max:
    most_max = most_max + l1

if l_avg - l_min == l_max - l_avg:
    print("YES")
else:
    print("NO")

# 3 lines are entered in random order.
# The program finds out whether it is possible to build an increasing
# arithmetic progression from the lengths of these strings.
