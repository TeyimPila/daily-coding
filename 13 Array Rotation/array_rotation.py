# def rotate_left(a, d):
#     for _ in range(d):
#
#         first_element = a[0]
#         for index in range(1, len(a)):
#             a[index - 1] = a[index]
#
#         a[-1] = first_element
#
#     return a


def rotate_left(a, d):
    length_of_array = len(a)
    rotated = a.copy()
    for i in range(length_of_array):
        new_location = (i + (length_of_array - d)) % length_of_array
        print(new_location)
        rotated[new_location] = a[i]

    return rotated


result = rotate_left([1, 2, 3, 4, 5], 4)

print(result)
