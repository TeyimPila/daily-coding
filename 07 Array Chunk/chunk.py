import math

"""
DIRECTIONS:
Given an array and chunk size, divide the array into many subarrays where each subarray is of length chunk size

EXAMPLES:
chunk([1,2,3,4,5], 2) --> [[1,2], [3,4], [5]]
"""


def chunk(arr, chunk_size):
    chunk_count = math.ceil(len(arr) / chunk_size)
    output = []
    for i in range(chunk_count):
        start = i * chunk_size
        stop = (i + 1) * chunk_size
        _chunk = arr[start: stop]
        output.append(_chunk)

    return output


result = chunk([1, 2, 3, 4], 1)

print(result)


def chunk_v2(arr, chunk_size):
    chunk_count = math.ceil(len(arr) / chunk_size)
    output = []
    for i in range(chunk_count):
        _chunk = arr[: chunk_size]
        output.append(_chunk)
        del (arr[: chunk_size])
    return output


result = chunk_v2([1, 2, 3, 4], 8)

print(result)


def chunk_v3(arr, chunk_size):
    chunked = []

    for element in arr:
        current_chunk = [] if len(chunked) == 0 else chunked[len(chunked) - 1]

        if current_chunk == [] or len(current_chunk) == chunk_size:
            chunked.append([element])
        else:
            current_chunk.append(element)
    return chunked


result = chunk_v3([1, 2, 3, 4], 3)
print(result)


