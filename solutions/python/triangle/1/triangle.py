def equilateral(sides):
    for side in sides:
        if side <= 0:
            return False
    if (sides[0] + sides[1] < sides[2]) or (sides[1] + sides[2] < sides[0]) or (sides[2] + sides[0] < sides[1]):
        return False
    if sides[1] == sides[0] and sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    for side in sides:
        if side <= 0:
            return False
    if (sides[0] + sides[1] < sides[2]) or (sides[1] + sides[2] < sides[0]) or (sides[2] + sides[0] < sides[1]):
        return False
    if sides[1] == sides[0] or sides[1] == sides[2] or sides[2] == sides[0]:
        return True
    return False


def scalene(sides):
    for side in sides:
        if side <= 0:
            return False
    if (sides[0] + sides[1] < sides[2]) or (sides[1] + sides[2] < sides[0]) or (sides[2] + sides[0] < sides[1]):
        return False
    if sides[1] != sides[0] and sides[0] != sides[2] and sides[1] != sides[2]:
        return True
    return False
