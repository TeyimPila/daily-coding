import re

"""
DIRECTIONS:
Check to see if two provided string are anagrams of each other.
One string is an anagram of another if it uses the same characters
in the same quantity. Only consider characters, not spaces or punctuation.
Consider capital letter to be the same as lower case

"""


def get_char_map(str):
    str = clean_string(str)
    char_map = {}

    for char in str:
        char_map[char] = 1 if char not in char_map else char_map[char] + 1

    return char_map


def clean_string(str):
    return re.sub("[\W]", '', str).lower()


def anagrams(string_a, string_b):
    if len(clean_string(string_a)) != len(clean_string(string_b)):
        return False

    a_char_map = get_char_map(string_a)
    b_char_map = get_char_map(string_b)

    for key in a_char_map.keys():
        if a_char_map[key] != b_char_map[key]:
            return False
    return True


print(anagrams("Hello! na88**", "Hello there?"))  # false
print(anagrams('rail safety!', 'FaIRY ^Tales!!'))  # True
