import math


def steps(n):
    for i in range(1, n + 1):
        print("#" * i + ' ' * (n - i))


def triangle(n):
    for i in range(1, n + 1):
        spaces = ' ' * math.ceil((n - i) / 2)
        if i % 2 == 1:
            print(spaces + "#" * i + spaces)


def recursive_steps(n, row=0, stair=''):
    if n == row:
        return

    if len(stair) == n:
        print(stair)
        return recursive_steps(n, row + 1)

    stair += '#' if len(stair) < row else ' '
    recursive_steps(n, row, stair)


#
# steps(5)
# triangle(11)
#
# steps(5)
# triangle(11)

recursive_steps(6)
