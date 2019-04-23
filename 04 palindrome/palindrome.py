"""
--Direction
Given a string, return a new string with
the reversed order of characters.

---Example
reverse('apple') === 'leppa'
"""


# Solution

def reverse(string):
    result = ''
    for index in reversed(range(len(string))):
        result += string[index]
    return result


def reverse_v2(string):
    result = ''
    string_len = len(string)
    for index in range(1, string_len + 1):
        reversed_index = string_len - index
        result += string[reversed_index]
    return result

def reverse_v3(string):
    reversed = ''
    for char in string:
       reversed = char + reversed
    return reversed

print(reverse('apple'))

print(reverse_v2('apple'))
print(reverse_v3('apple'))


def reverse(num):
    result = 0

    digits = digits_count(num)

    for power in reversed(range(digits)):
        last_digit = num%10
        order_last_digit = last_digit * 10**power
        result += order_last_digit

        num = num//10

    return result





def digits_count(x):
    """
    Assumes int(x)
    """

    x = abs(x)

    if x < 10:
        return 1

    return 1 + digits_count(x / 10)

print(reverse(-12345000))

