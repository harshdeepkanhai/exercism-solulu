def is_armstrong_number(number):
    n = len(str(number))
    if sum([int(digit)**n for digit in str(number)]) == number:
        return True
    return False
