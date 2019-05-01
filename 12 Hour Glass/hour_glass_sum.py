def hourglass_sum(arr):
    arr = [row.strip().split(" ") for row in arr.strip().split("\n")]

    max_hour = 0
    first = False
    for row in range(len(arr) - 2):
        for column in range(len(arr) - 2):
            top = [int(element) for element in arr[row][column: column + 3]]
            middle = int(arr[row + 1][column + 1])
            bottom = [int(element) for element in arr[row + 2][column: column + 3]]

            hour = sum(top) + middle + sum(bottom)

            if not first:
                max_hour = hour
                first = True

            max_hour = hour if hour > max_hour else max_hour

    return max_hour


print(hourglass_sum(
    """
    -1 -1 0 -9 -2 -2
    -2 -1 -6 -8 -2 -5
    -1 -1 -1 -2 -3 -4
    -1 -9 -2 -4 -4 -5
    -7 -3 -3 -2 -9 -9
    -1 -3 -1 -2 -4 -5
    """
))
