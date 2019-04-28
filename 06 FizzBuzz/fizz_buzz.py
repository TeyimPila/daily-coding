"""
given a real number, print all numbers up to and including that number.
If any of the numbers is a multiple of 3, print fizz, it is a multiple
of 5, print buzz if it is a multiple of 5 and 5, print fizzbuzz
"""


def fizz_buzz(n):
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 != 0:
            print("{0} ==> fizz".format(number))
        if number % 5 == 0 and number % 3 != 0:
            print("{0} ==> buzz".format(number))
        if number % 15 == 0:
            print("{0} ==> fizzbuzz".format(number))


fizz_buzz(15)
