
"""
See Problem statement here on hackerrank:
https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""
def minimum_swaps(arr):
    arr = [element - 1 for index, element in enumerate(arr)]
    swap = 0
    print(arr)

    for i in range(len(arr)):

        # While the current element hasn't reached its rightful position, continue swapping.
        while i != arr[i]:
            swap += 1
            j = arr[i]
            arr[i], arr[j] = arr[j], arr[i]
            print(arr)
        i += 1
    return swap


print(minimum_swaps([7, 1, 3, 2, 4, 5, 6]))
