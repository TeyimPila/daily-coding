import math


def steps(n):
    for i in range(1, n + 1):
        print("#" * i + ' ' * (n - i))


def triangle(n):
    for i in range(1, n + 1):
        spaces = ' ' * math.ceil((n - i) / 2)
        if i % 2 == 1:
            print(spaces + "#" * i + spaces)



steps(5)
triangle(11)

steps(5)
triangle(11)
