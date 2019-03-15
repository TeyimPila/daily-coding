"""
Good morning! Here's your coding interview problem for today.

This problem was recently asked by Google.

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?
"""


# THE BRUTE FORCE APPROACH
def contains_sum_k(arr, k):
    """
    This is a simplet python function that return True if
    there is a pair of numbers in the list, arr that add
    up to the number, k, and false otherwise

    :param arr:
    :param k:
    :return True | False:
    """
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i] + arr[j] == k:
                return True
    return False

# Example
result = contains_sum_k([1,6,2,3,4,5], 10)
print(result) # True

# THE BETTER IMPLEMENTATION THAT USES O(N) SPACE COMPLEXITY
"""
Since we are looking for:
    any x,y in A 
    such that x+y=k, 
This means if we can find:
    any x in A 
    such that k-x=y 
    where y is also in A, 
    then x and y sum up to k
"""

def contains_k_complements(arr, k):
    for index in range(len(arr)):
        if(k - arr[index] in arr):
            return True
    return False

# Example
result = contains_k_complements([1,6,2,3,4,5], 10)
print(result) # True

