def is_armstrong_number(number):
    n = str(number)
    return sum([int(digit)**len(n) for digit in n]) == number
