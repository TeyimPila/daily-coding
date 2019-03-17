"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i
of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
"""


def resulting_product_arr(arr):
    product = 1
    result = []

    for i in arr:
        product *= i

    for j in range(len(arr)):
        result.append(product // arr[j])

    return result


print(resulting_product_arr([1, 2, 3, 4, 5]))


"""
What if you can't use division?
"""


def prod_above_index(i, arr):
    product = 1
    for i in range((i + 1), len(arr)):
        product *= arr[i]
    return product


def prod_before_index(index, arr):
    product = 1
    for i in range(index):
        product *= arr[i]
    return product


def products_of_rest(arr):
    result = []
    for i in range(len(arr)):
        prod_before = prod_before_index(i, arr)
        prod_after = prod_above_index(i, arr)
        result.append(prod_before * prod_after)
    return result


print(products_of_rest([1, 2, 3, 4, 5]))
