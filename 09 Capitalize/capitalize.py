import re


def capitalize(string):
    string_arr = string.split(' ')

    capitalized = ''

    for word in string_arr:
        word = word.capitalize()
        capitalized += word + ' '
    return capitalized


print(capitalize("This should!, change"))
print(capitalize("A shorT sentence"))


def capitalize_v2(string):
    string_arr = string.split(' ')

    for word in string_arr:
        string = re.sub(word, word.capitalize(), string)
    return string


print(capitalize_v2("This should!, change"))
print(capitalize_v2("A shorT sentence"))
