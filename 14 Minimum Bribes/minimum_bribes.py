def minimum_bribes(q):
    bribes = 0

    q = [element - 1 for element in q]

    for i, person in enumerate(q):
        if person - i > 2:
            print("Too chaotic")
            return

        for j in range(max(0, person - 2), i):
            if q[j] > person:
                bribes += 1

    return bribes


bribe_count = minimum_bribes([2, 1, 5, 3, 4])
print(bribe_count)

bribe_count = minimum_bribes([2, 5, 1, 3, 4])
print(bribe_count)

"""
1 2 3 4 5 6 7 8

1 2 3 5 4 6 7 8

1 2 5 3 4 6 7 8

1 2 5 3 4 7 6 8

1 2 5 3 7 4 6 8

1 2 5 3 7 6 4 8

1 2 5 3 7 6 8 4

1 2 5 3 7 8 6 4
"""

bribe_count = minimum_bribes([1, 2, 5, 3, 7, 8, 6, 4])
print(bribe_count)
