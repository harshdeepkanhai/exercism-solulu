resistors_dict = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

def value(colors):
    band_values = [resistors_dict[colors[i].lower()] for i in range(2)]
    return int("".join(str(x) for x in band_values))