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
