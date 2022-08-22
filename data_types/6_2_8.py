town1, town2, town3 = input(), input(), input()

l1 = len(town1)
l2 = len(town2)
l3 = len(town3)

town_min = min(l1, l2, l3)
town_max = max(l1, l2, l3)

if town_min == l1:
    print(town1)
elif town_min == l2:
    print(town2)
elif town_min == l3:
    print(town3)

if town_max == l1:
    print(town1)
elif town_max == l2:
    print(town2)
elif town_max == l3:
    print(town3)

# The names of three cities are given. The program determines the shortest and longest city name.
