"""
Return the character with the highest frequency
"""


def char_freq(string):
    string = string.lower()
    map = {}
    max = 0
    maxChar = ''

    for char in string:
        if map.get(char):
            map[char] +=1
        else:
            map[char] = 1

    for key in map:
        if map[key] > max:
            max = map[key]
            maxChar = key

    return maxChar


print(char_freq("Heo hello"))
