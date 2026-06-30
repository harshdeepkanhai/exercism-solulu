"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    if all(i in list_two for i in list_one) and ",".join([str(i) for i in list_one]) in ",".join([str(i) for i in list_two]) :
        return SUBLIST
    if all(i in list_one for i in list_two) and ",".join([str(i) for i in list_two]) in ",".join([str(i) for i in list_one]) :
        return SUPERLIST
    return UNEQUAL
