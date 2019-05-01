def jumps(c):
    arr = [int(element) for element in c.split(' ')]

    steps = 0
    i = 0
    while i < len(arr) - 3:
        if arr[i + 2] == 0:
            i += 2
        else:
            i += 1
        steps += 1

    return steps+1


print(jumps('0 0 1 0 0 0 0 0 1 0 1 0 1 0 0 0 1'))
