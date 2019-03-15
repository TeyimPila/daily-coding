"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def resulting_product_arr(arr):
    product = 1
    result = []

    for i in arr:
        product *= i

    for j in range(len(arr)):
        print(j)
        result.append(product // arr[j])

    return result


output = resulting_product_arr([1, 2, 3, 4, 5])

print(output)

"""
To be continued: what if you can't use division?
"""
